# ============================================================
# RE: MERCENARY - SCRIPT PRINCIPAL
# ============================================================
default turno_jugador = True
default jugador_x = 0
default jugador_y = 0
default destino_x = 0
default destino_y = 0
default heroe_actual = None
default heroes = []
default unidad_seleccionada = None
default texto_turno = "Tu turno"
default ejercito = []
default maxima_cantidad_unidades = 8
default enemigos = []
default enemigos_iniciales = []
default partida_terminada = False
default resultado_batalla = ""
default nivel_actual = 0
default partida_guardada = False
default seleccion_heroe = True
default slot_guardado = "partida"
default boss_musica_activada = False
default boss_spawneado = False
default modo_versus = False
default ejercito_j1 = []
default ejercito_j2 = []
default turno_actual = 1

image pantalla_inicio = "pantalla_inicio.png"
image portada = "portada.png"

init python:
    import random
    COLUMNAS = 8
    FILAS = 5
    OFFSET_X = 180
    OFFSET_Y = 140
    CASILLA_W = 195
    CASILLA_H = 170

init python:
    def registrar_habilidad_usada():
        pass

    def get_stats_personaje(personaje):
        hp = personaje.get_vida()
        hp_max = personaje.get_vida_max()
        texto = "HP: " + str(hp) + "/" + str(hp_max)
        try:
            if isinstance(personaje, (store.Mago, store.ArchiMago, store.Lich, store.Clerigo, store.Dragon)):
                texto += " | MAGIA: " + str(personaje.get_magia()) + "/" + str(personaje.get_magia_max())
            elif isinstance(personaje, store.Arquero):
                texto += " | FLECHAS: " + str(personaje.get_carcaj()) + " | ESP: " + str(personaje.get_flecha_trucada())
            elif isinstance(personaje, store.General):
                texto += " | ENERGIA: " + str(personaje.get_energia())
            elif isinstance(personaje, store.Guerrero):
                texto += " | ATQ: " + str(personaje.get_ataque_basico()) + " | DEF: " + str(personaje.get_defensa())
        except:
            pass
        return texto

    def aplicar_danio_basico(atacante, defensor):
        atk = atacante.get_ataque_basico()
        dfs = defensor.get_defensa()
        danio = max(5, int(atk - (dfs * 0.5)))
        nueva_vida = max(0, defensor.get_vida() - danio)
        defensor.set_vida(nueva_vida)
        return danio

    def aplicar_danio_magico(atacante, defensor, multiplicador):
        atk = atacante.get_ataque_basico()
        dfs = defensor.get_defensa()
        danio = max(5, int((atk * multiplicador) - (dfs * 0.5)))
        nueva_vida = max(0, defensor.get_vida() - danio)
        defensor.set_vida(nueva_vida)
        return danio

# ============================================================
# MOVIMIENTO DE ENEMIGOS - PARA QUE LA IA SE MUEVA
# ============================================================
init python:
    def mover_enemigos():
        for enemigo in store.enemigos[:]:
            if not enemigo.get_visible() or not enemigo.esta_vivo():
                continue

            objetivo = None
            menor_dist = 9999
            for h in store.heroes + store.ejercito:
                if h.get_visible() and h.esta_vivo():
                    dist = abs(h.get_x() - enemigo.get_x()) + abs(h.get_y() - enemigo.get_y())
                    if dist < menor_dist:
                        menor_dist = dist
                        objetivo = h

            if objetivo is None:
                continue

            ex, ey = enemigo.get_x(), enemigo.get_y()
            hx, hy = objetivo.get_x(), objetivo.get_y()

            opciones = []
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = ex + dx, ey + dy
                if nx < 0 or nx >= COLUMNAS or ny < 0 or ny >= FILAS:
                    continue
                ocupada = False
                for otra in store.enemigos + store.heroes + store.ejercito:
                    if otra != enemigo and otra.get_visible() and otra.esta_vivo():
                        if otra.get_x() == nx and otra.get_y() == ny:
                            ocupada = True
                            break
                if not ocupada:
                    nueva_dist = abs(nx - hx) + abs(ny - hy)
                    opciones.append((nueva_dist, nx, ny))

            if opciones:
                opciones.sort()
                _, nx, ny = opciones[0]
                enemigo.set_x(nx)
                enemigo.set_y(ny)
                print("[MOV] " + enemigo.get_clase() + " -> (" + str(nx) + "," + str(ny) + ")")

init python:
    def crear_heroes():
        return [Kazuki(2, 3), Lyra(4, 3), Gromm(6, 3)]

init python:
    def quedan_enemigos_vivos():
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo():
                return True
        return False

    def quedan_heroes_vivos():
        for heroe in store.heroes:
            if heroe.esta_vivo():
                return True
        return False

    def hay_unidades_vivas(ejercito):
        for unidad in ejercito:
            if unidad.get_visible() and unidad.esta_vivo():
                return True
        return False

    def contar_esbirros_vivos():
        contador = 0
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo() and not es_boss(enemigo.get_clase()):
                contador += 1
        return contador

    def contar_bosses_vivos():
        contador = 0
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo() and es_boss(enemigo.get_clase()):
                contador += 1
        return contador

    def cambiar_turno():
        if store.turno_actual == 1:
            store.turno_actual = 2
            store.texto_turno = "Turno Jugador 2"
        else:
            store.turno_actual = 1
            store.texto_turno = "Turno Jugador 1"
        store.unidad_seleccionada = None

    def guardar_partida(slot="partida"):
        renpy.save(slot)
        store.partida_guardada = True
        store.slot_guardado = slot
        renpy.notify("Partida guardada.")

    def verificar_combate_cercano():
        heroe = store.heroe_actual
        if heroe is None or not heroe.esta_vivo():
            return None
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo() and enemigo.get_x() == heroe.get_x() and enemigo.get_y() == heroe.get_y():
                return enemigo
        return None

    def verificar_combate_adyacente(heroe):
        if heroe is None or not heroe.esta_vivo():
            return None
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo():
                dist = abs(enemigo.get_x() - heroe.get_x()) + abs(enemigo.get_y() - heroe.get_y())
                if dist <= 1:
                    return enemigo
        return None

# ============================================================
# CLICK EN CASILLA
# ============================================================
init python:
    def click_casilla(x, y):
        if not store.turno_jugador:
            renpy.notify("Turno enemigo")
            return

        enemigo_encima = verificar_combate_cercano()
        if enemigo_encima is not None:
            renpy.call_in_new_context("combate", store.heroe_actual, enemigo_encima)
            store.unidad_seleccionada = None
            return

        for heroe in store.heroes:
            if heroe.get_visible() and heroe.esta_vivo() and heroe.get_x() == x and heroe.get_y() == y:
                store.unidad_seleccionada = heroe
                store.heroe_actual = heroe
                renpy.notify("Seleccionado: " + heroe.get_clase())
                return

        for unidad in store.ejercito:
            if unidad.get_visible() and unidad.esta_vivo() and unidad.get_x() == x and unidad.get_y() == y:
                store.unidad_seleccionada = unidad
                store.heroe_actual = unidad
                renpy.notify("Seleccionado: " + unidad.get_clase())
                return

        if store.unidad_seleccionada is None:
            return

        unidad = store.unidad_seleccionada
        dx = abs(x - unidad.get_x())
        dy = abs(y - unidad.get_y())

        if dx + dy != 1:
            renpy.notify("Solo puedes mover 1 casilla")
            return

        for otra in store.ejercito + store.heroes:
            if otra != unidad and otra.get_visible() and otra.get_x() == x and otra.get_y() == y:
                renpy.notify("Esta casilla esta ocupada!")
                return

        unidad.set_x(x)
        unidad.set_y(y)
        store.jugador_x = x
        store.jugador_y = y

        enemigo_encima = verificar_combate_cercano()
        if enemigo_encima is not None:
            renpy.call_in_new_context("combate", store.heroe_actual, enemigo_encima)
            store.unidad_seleccionada = None
            return

        renpy.notify("Turno enemigo")
        store.turno_jugador = False
        store.texto_turno = "Turno enemigo"

        mover_enemigos()

        parejas = []
        for heroe in store.heroes:
            if heroe.get_visible() and heroe.esta_vivo():
                enemigo = verificar_combate_adyacente(heroe)
                if enemigo is not None:
                    parejas.append((heroe, enemigo))

        for heroe, enemigo in parejas:
            if heroe.esta_vivo() and enemigo.esta_vivo():
                store.heroe_actual = heroe
                renpy.call_in_new_context("combate", heroe, enemigo)
                if not quedan_heroes_vivos():
                    store.resultado_batalla = "derrota"
                    store.partida_terminada = True
                    return

        if not quedan_enemigos_vivos() and not store.boss_spawneado:
            if store.nivel_actual >= 1 and store.nivel_actual <= 7:
                bx, by = 4, 0
                nuevo_boss = crear_boss_por_nivel(store.nivel_actual, bx, by)
                if nuevo_boss is not None:
                    store.enemigos.append(nuevo_boss)
                    store.boss_spawneado = True
                    try:
                        reproducir_musica("Boss" + str(store.nivel_actual) + ".wav", fadein=0.5, loop=True)
                    except:
                        pass
                    renpy.notify("EL BOSS HA APARECIDO!")

        if store.boss_spawneado and not quedan_enemigos_vivos():
            store.resultado_batalla = "victoria"
            store.partida_terminada = True
            return

        if not quedan_heroes_vivos():
            store.resultado_batalla = "derrota"
            store.partida_terminada = True
            return

        store.turno_jugador = True
        store.texto_turno = "Tu turno"
        store.unidad_seleccionada = None
        renpy.notify("Tu turno")

init python:
    def click_casilla_versus(x, y):
        if store.turno_actual == 1:
            ejercito_actual = store.ejercito_j1
            ejercito_rival = store.ejercito_j2
        else:
            ejercito_actual = store.ejercito_j2
            ejercito_rival = store.ejercito_j1

        for unidad in ejercito_actual:
            if unidad.get_visible() and unidad.esta_vivo() and unidad.get_x() == x and unidad.get_y() == y:
                store.unidad_seleccionada = unidad
                renpy.notify("Seleccionado: " + unidad.get_clase())
                return

        if store.unidad_seleccionada is None:
            return

        if store.unidad_seleccionada not in ejercito_actual:
            renpy.notify("Esa unidad no es tuya!")
            return

        unidad = store.unidad_seleccionada
        dx = abs(x - unidad.get_x())
        dy = abs(y - unidad.get_y())

        if dx + dy != 1:
            renpy.notify("Solo puedes mover 1 casilla")
            return

        for otra in ejercito_actual:
            if otra != unidad and otra.get_visible() and otra.get_x() == x and otra.get_y() == y:
                renpy.notify("Casilla ocupada por aliado!")
                return

        for enemigo in ejercito_rival:
            if enemigo.get_visible() and enemigo.esta_vivo() and enemigo.get_x() == x and enemigo.get_y() == y:
                renpy.call_in_new_context("combate_versus", unidad, enemigo)
                cambiar_turno()
                if not hay_unidades_vivas(store.ejercito_j1):
                    store.resultado_batalla = "j2_gana"
                    store.partida_terminada = True
                    return
                if not hay_unidades_vivas(store.ejercito_j2):
                    store.resultado_batalla = "j1_gana"
                    store.partida_terminada = True
                    return
                return

        unidad.set_x(x)
        unidad.set_y(y)
        store.unidad_seleccionada = None
        cambiar_turno()

        if not hay_unidades_vivas(store.ejercito_j1):
            store.resultado_batalla = "j2_gana"
            store.partida_terminada = True
            return
        if not hay_unidades_vivas(store.ejercito_j2):
            store.resultado_batalla = "j1_gana"
            store.partida_terminada = True
            return

# ============================================================
# COMBATE
# ============================================================
label combate(heroe, enemigo):
    python:
        ia = None
        clase_enemigo = enemigo.get_clase()
        if "Archimago" in clase_enemigo: ia = IA_ArchiMago()
        elif "Lich" in clase_enemigo: ia = IA_Lich()
        elif "Clerigo" in clase_enemigo: ia = IA_Clerigo()
        elif "Guerrero" in clase_enemigo: ia = IA_Guerrero()
        elif "Arquero" in clase_enemigo: ia = IA_Arquero()
        elif "Dragon" in clase_enemigo: ia = IA_Dragon()
        elif "Mago" in clase_enemigo: ia = IA_Mago()
        elif "General" in clase_enemigo: ia = IA_General()
        else: ia = None

    while heroe.esta_vivo() and enemigo.esta_vivo():
        $ nombre_enemigo = enemigo.get_clase()
        $ nombre_heroe = heroe.get_clase()
        $ stats_heroe = get_stats_personaje(heroe)
        $ stats_enemigo = get_stats_personaje(enemigo)
        "[nombre_heroe]: [stats_heroe]"
        "[nombre_enemigo]: [stats_enemigo]"

        $ clase = heroe.get_clase()
        $ accion_realizada = False

        # ============================================
        # KAZUKI
        # ============================================
        if clase == "Kazuki":
            $ info_k = "Kazuki - MAGIA: " + str(heroe.get_magia()) + "/" + str(heroe.get_magia_max())
            menu:
                "[info_k]"
                "Atacar (Bola de Fuego) - 100 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "BOLA DE FUEGO! [danio] de danio."
                "Bola de Fuego Mejorada - 200 magia":
                    $ danio = heroe.bola_fuego_mejorada(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Bola Mejorada! [danio] de danio."
                "Ataque Hielo Infernal - 100 magia":
                    $ danio = heroe.ataque_hielo_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Hielo Infernal! [danio] de danio."
                "Castigo Divino - 300 magia":
                    $ danio = heroe.ataque_castigo_divino(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Castigo Divino! [danio] de danio."
                "Vientos Infernales - 500 magia":
                    $ danio = heroe.vientos_infernales_prohibidos(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Vientos Infernales! [danio] de danio."
                "Waldgose - 1000 magia":
                    $ danio = heroe.ataque_magico_prohibido(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "WALDGOSE! [danio] de danio."
                "Potenciar aliado (+20% ATQ)":
                    $ heroe.potenciar_aliado(heroe)
                    $ accion_realizada = True
                    "Kazuki se potencia! ATQ: [heroe.get_ataque_basico()]"
                "Curacion Magica - 290 magia":
                    $ curado = heroe.curacion_magica()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Recuperar Magia +100":
                    $ heroe.recuperar_magia(100)
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # LYRA
        # ============================================
        elif clase == "Lyra":
            $ info_l = "Lyra - FLECHAS: " + str(heroe.get_carcaj()) + " | ESP: " + str(heroe.get_flecha_trucada())
            menu:
                "[info_l]"
                "Disparar Flecha (1 flecha)":
                    $ danio = heroe.disparar_flechas(enemigo)
                    if danio == 0:
                        "No tienes flechas!"
                    else:
                        $ accion_realizada = True
                        "Disparo! [danio] de danio. Flechas: [heroe.get_carcaj()]"
                "Flecha Perforante (1 esp)":
                    $ danio = heroe.flecha_perforante(enemigo)
                    if danio == 0:
                        "No tienes flechas!"
                    else:
                        $ accion_realizada = True
                        "PERFORANTE! [danio] de danio."
                "Flecha de Hielo (1 esp)":
                    $ danio = heroe.flecha_de_hielo(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Hielo! [danio] de danio."
                "Flecha Venenosa (1 esp)":
                    $ danio = heroe.flecha_venenosa(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Venenosa! [danio] de danio."
                "Flecha Explosiva (1 esp)":
                    $ danio = heroe.flecha_explosiva(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "EXPLOSIVA! [danio] de danio."
                "Flecha Electrica (1 esp)":
                    $ danio = heroe.flecha_electrica(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Electrica! [danio] de danio."
                "Tiro Doble (2 flechas + 2 esp)":
                    $ danio = heroe.tiro_doble(enemigo)
                    if danio == 0:
                        "No tienes suficientes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Tiro Doble! [danio] de danio."
                "Recargar Carcaj":
                    $ heroe.recarga_rapida()
                    $ accion_realizada = True
                    "Recargas. Flechas: [heroe.get_carcaj()] Esp: [heroe.get_flecha_trucada()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # GROMM
        # ============================================
        elif clase == "Gromm":
            $ info_g = "Gromm - ATQ: " + str(heroe.get_ataque_basico()) + " | DEF: " + str(heroe.get_defensa())
            menu:
                "[info_g]"
                "Atacar":
                    $ danio = heroe.ataque_basico(enemigo)
                    $ accion_realizada = True
                    "Golpe! [danio] de danio."
                "Testudo (+DEF x2)":
                    $ heroe.testudo()
                    $ accion_realizada = True
                    "DEF: [heroe.get_defensa()]"
                "Arremeter (+20 ATQ)":
                    $ heroe.arremeter()
                    $ accion_realizada = True
                    "ATQ: [heroe.get_ataque_basico()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # MAGO
        # ============================================
        elif clase in ["Mago", "Mago2"]:
            $ info_m = "Mago - MAGIA: " + str(heroe.get_magia()) + "/" + str(heroe.get_magia_max())
            menu:
                "[info_m]"
                "Ataque basico - 100 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Bola de Fuego Mejorada - 200 magia":
                    $ danio = heroe.bola_fuego_mejorada(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Bola! [danio] de danio."
                "Hielo Infernal - 100 magia":
                    $ danio = heroe.ataque_hielo_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Hielo! [danio] de danio."
                "Castigo Divino - 300 magia":
                    $ danio = heroe.ataque_castigo_divino(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Castigo! [danio] de danio."
                "Vientos Infernales - 500 magia":
                    $ danio = heroe.vientos_infernales_prohibidos(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Vientos! [danio] de danio."
                "Waldgose - 1000 magia":
                    $ danio = heroe.ataque_magico_prohibido(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "WALDGOSE! [danio] de danio."
                "Curacion Magica - 290 magia":
                    $ curado = heroe.curacion_magica()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Recuperar Magia +100":
                    $ heroe.recuperar_magia(100)
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # ARCHIMAGO
        # ============================================
        elif clase in ["Archimago", "Archimago2"]:
            $ info_a = "Archimago - MAGIA: " + str(heroe.get_magia()) + "/" + str(heroe.get_magia_max())
            menu:
                "[info_a]"
                "Ataque basico - 100 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Ataque Especial - 300 magia":
                    $ danio = heroe.ataque_especial(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Especial! [danio] de danio."
                "Ataque Gelido - 259 magia":
                    $ danio = heroe.ataque_gelido(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Gelido! [danio] de danio."
                "Ataque Oscuro - 360 magia":
                    $ danio = heroe.ataque_oscuro(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Oscuro! [danio] de danio."
                "Espadas de Luz - 500 magia":
                    $ danio = heroe.ataque_espadas_magicas_de_luz(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espadas! [danio] de danio."
                "Relampago - 365 magia":
                    $ danio = heroe.ataque_magico_relampago(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Relampago! [danio] de danio."
                "Ataque Final - 1000 magia":
                    $ danio = heroe.ataque_final(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "FINAL! [danio] de danio."
                "Curacion Magica - 290 magia":
                    $ curado = heroe.curacion_magica()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Recuperar Magia +200":
                    $ heroe.recuperar_magia(200)
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # GUERRERO
        # ============================================
        elif clase in ["Guerrero", "Guerrero2"]:
            $ info_gu = "Guerrero - ATQ: " + str(heroe.get_ataque_basico()) + " | DEF: " + str(heroe.get_defensa())
            menu:
                "[info_gu]"
                "Atacar":
                    $ danio = heroe.ataque_basico(enemigo)
                    $ accion_realizada = True
                    "Atacas. [danio] de danio."
                "Testudo (+DEF x2)":
                    $ heroe.testudo()
                    $ accion_realizada = True
                    "DEF: [heroe.get_defensa()]"
                "Arremeter (+20 ATQ)":
                    $ heroe.arremeter()
                    $ accion_realizada = True
                    "ATQ: [heroe.get_ataque_basico()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # ARQUERO
        # ============================================
        elif clase in ["Arquero", "Arquero2"]:
            $ info_ar = "Arquero - FLECHAS: " + str(heroe.get_carcaj()) + " | ESP: " + str(heroe.get_flecha_trucada())
            menu:
                "[info_ar]"
                "Disparar Flecha":
                    $ danio = heroe.disparar_flechas(enemigo)
                    if danio == 0:
                        "No tienes flechas!"
                    else:
                        $ accion_realizada = True
                        "Disparas. [danio] de danio. Flechas: [heroe.get_carcaj()]"
                "Flecha Especial":
                    $ danio = heroe.flechita_especial(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Especial! [danio] de danio."
                "Flecha de Hielo":
                    $ danio = heroe.flecha_de_hielo(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Hielo! [danio] de danio."
                "Flecha Venenosa":
                    $ danio = heroe.flecha_venenosa(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Venenosa! [danio] de danio."
                "Tiro Doble":
                    $ danio = heroe.tiro_doble(enemigo)
                    if danio == 0:
                        "No tienes flechas o esp!"
                    else:
                        $ accion_realizada = True
                        "Tiro Doble! [danio] de danio."
                "Recargar":
                    $ heroe.recarga_rapida()
                    $ accion_realizada = True
                    "Recargas. Flechas: [heroe.get_carcaj()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # LICH
        # ============================================
        elif clase in ["Lich", "Lich2"]:
            $ info_li = "Lich - MAGIA: " + str(heroe.get_magia()) + "/" + str(heroe.get_magia_max())
            menu:
                "[info_li]"
                "Ataque basico - 100 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Ataque Espectral - 50 magia":
                    $ danio = heroe.ataque_espectral(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espectral! [danio] de danio."
                "Drenar Vida - 30 magia":
                    $ danio = heroe.drenar_vida(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Drenar! [danio] de danio. HP: [heroe.get_vida()]"
                "Ataque Masivo - 100 magia":
                    $ danio = heroe.ataque_masivo(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Masivo! [danio] de danio."
                "Curar - 40 magia":
                    $ curado = heroe.curar()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Regenerar Magia":
                    $ restaurado = heroe.regenerar_magia()
                    $ accion_realizada = True
                    "MAGIA restaurada: [restaurado]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # CLERIGO
        # ============================================
        elif clase in ["Clerigo", "Clerigo2"]:
            $ info_cl = "Clerigo - MAGIA: " + str(heroe.get_magia()) + "/" + str(heroe.get_magia_max())
            menu:
                "[info_cl]"
                "Ataque basico - 100 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Palabras de Fe - 100 magia":
                    $ resultado = heroe.palabras_de_fe(enemigo)
                    if resultado == False:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "ATQ enemigo reducido a [enemigo.get_ataque_basico()]"
                "Luz Cegadora - 300 magia":
                    $ danio = heroe.luz_cegadora_dia(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Luz! [danio] de danio."
                "Exorcismo - 400 magia":
                    $ danio = heroe.exorcismo(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "EXORCISMO! [danio] de danio."
                "Escudo de Fe - 200 magia":
                    $ resultado = heroe.escudo_de_fe_magico()
                    if resultado == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "DEF: [heroe.get_defensa()]"
                "Recuperar Magia +200":
                    $ heroe.recuperacion_sagrada(200)
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # GENERAL
        # ============================================
        elif clase in ["General", "General2"]:
            $ info_gen = "General - ENERGIA: " + str(heroe.get_energia())
            menu:
                "[info_gen]"
                "Espada - 100 energia":
                    $ danio = heroe.espada(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia! Recuperas 200."
                    else:
                        $ accion_realizada = True
                        "Corte! [danio] de danio. ENERGIA: [heroe.get_energia()]"
                "Canon de Mano - 250 energia":
                    $ danio = heroe.canon_de_mano(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia!"
                    else:
                        $ accion_realizada = True
                        "Canon! [danio] de danio. ENERGIA: [heroe.get_energia()]"
                "Tiro Doble - 350 energia":
                    $ danio = heroe.tiro_doble(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia!"
                    else:
                        $ accion_realizada = True
                        "Tiro Doble! [danio] de danio. ENERGIA: [heroe.get_energia()]"
                "Carga de Caballeria":
                    $ danio = heroe.carga_de_caballeria(enemigo, 2)
                    $ accion_realizada = True
                    "Carga! [danio] de danio."
                "Canon Final - 1000 energia":
                    $ danio = heroe.canion_especial_final(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia!"
                    else:
                        $ accion_realizada = True
                        "CANON FINAL! [danio] de danio."
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # DRAGON
        # ============================================
        elif clase in ["Dragon", "Dragon2"]:
            $ info_dr = "Dragon - MAGIA: " + str(heroe.get_magia()) + "/" + str(heroe.get_magia_max())
            menu:
                "[info_dr]"
                "Ataque basico - 100 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Golpe! [danio] de danio."
                "Llamarada Infernal - 200 magia":
                    $ danio = heroe.ataque_llamarada_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Llamarada! [danio] de danio."
                "Ataque de Espinas - 100 magia":
                    $ danio = heroe.ataque_espinas(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espinas! [danio] de danio."
                "Rayo de Luz - 150 magia":
                    $ danio = heroe.ataque_luz(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Rayo de Luz! [danio] de danio."
                "Escamas Reflectantes - 30 magia":
                    $ resultado = heroe.escamas_reflectantes()
                    if resultado == False:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Escamas activadas!"
                "Regeneracion":
                    $ restaurado = heroe.regeneracion_dragon()
                    $ accion_realizada = True
                    "HP recuperado: [restaurado]"
                "Recuperar Magia +100":
                    $ heroe.recuperacion_draconica(100)
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        else:
            menu:
                "[clase] - Que haras?"
                "Atacar":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    $ accion_realizada = True
                    "Atacas. [danio] de danio."
                "Huir":
                    "Escapaste!"
                    return

        # MOSTRAR STATS ACTUALIZADOS DESPUES DE LA ACCION
        if accion_realizada:
            $ stats_post = get_stats_personaje(heroe)
            "[nombre_heroe] ahora tiene: [stats_post]"

        if not enemigo.esta_vivo():
            "[nombre_enemigo] HA SIDO DERROTADO!"
            $ enemigo.set_visible(False)
            return

        python:
            if ia is not None:
                try:
                    if "Clerigo" in enemigo.get_clase():
                        ia.evaluar(enemigo, heroe, store.enemigos)
                    else:
                        ia.evaluar(enemigo, heroe)
                except Exception as e:
                    print("[IA ERROR] " + str(e))
                    danio_enemigo = max(5, enemigo.get_ataque_basico() // 2)
                    heroe.set_vida(max(0, heroe.get_vida() - danio_enemigo))
                    renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")
            else:
                danio_enemigo = max(5, enemigo.get_ataque_basico() // 2)
                heroe.set_vida(max(0, heroe.get_vida() - danio_enemigo))
                renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")

        if not heroe.esta_vivo():
            $ nombre_heroe_muerto = heroe.get_clase()
            "[nombre_heroe_muerto] HA CAIDO!"
            $ heroe.set_visible(False)
            python:
                todos_muertos = True
                for h in store.heroes:
                    if h.esta_vivo():
                        todos_muertos = False
                        break
                if todos_muertos:
                    store.resultado_batalla = "derrota"
                    store.partida_terminada = True
            return
    return

# ============================================================
# COMBATE VERSUS
# ============================================================
label combate_versus(atacante, defensor):
    while atacante.esta_vivo() and defensor.esta_vivo():
        $ d = aplicar_danio_basico(atacante, defensor)
        "[atacante.get_clase()] ataca a [defensor.get_clase()] por [d] de danio!"

        if not defensor.esta_vivo():
            "[defensor.get_clase()] ha caido!"
            $ defensor.set_visible(False)
            return

        $ c = aplicar_danio_basico(defensor, atacante) // 2
        "[defensor.get_clase()] contraataca por [c] de danio!"

        if not atacante.esta_vivo():
            "[atacante.get_clase()] ha caido!"
            $ atacante.set_visible(False)
            return
    return

# ============================================================
# ARMAR EJERCITO
# ============================================================
label armar_ejercito:
    $ total = len(ejercito)

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (3, 4)]
        casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito]
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        if not casillas_disponibles:
            casillas_disponibles = [(0, 4)]
        px, py = random.choice(casillas_disponibles)

    if total >= maxima_cantidad_unidades:
        "Ya tenes [maxima_cantidad_unidades] unidades. Ahora elegi un nivel:"
        jump elegir_nivel
    else:
        menu:
            "Elegi una unidad para tu ejercito ([total]/[maxima_cantidad_unidades]):"
            "Mago":
                $ unidad = Mago("Mago", 200, 25, 15, 4, 3, 30, px, py, 0, True, 100, 100, 10, 10, 10)
                $ ejercito.append(unidad)
                "Agregaste un Mago."
                jump armar_ejercito
            "General":
                $ unidad = General("General", 250, 30, 20, 3, 2, 40, px, py, 0, True, 1000, 500)
                $ ejercito.append(unidad)
                "Agregaste un General."
                jump armar_ejercito
            "Archimago":
                $ unidad = ArchiMago("Archimago", 300, 35, 25, 3, 3, 50, px, py, 0, True, 1500, 100)
                $ ejercito.append(unidad)
                "Agregaste un Archimago."
                jump armar_ejercito
            "Guerrero":
                $ unidad = Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, px, py, 0, True)
                $ ejercito.append(unidad)
                "Agregaste un Guerrero."
                jump armar_ejercito
            "Dragon":
                $ unidad = Dragon("Dragon", 300, 60, 30, 2, 3, 70, px, py, 0, True, 500, 0, 0)
                $ ejercito.append(unidad)
                "Agregaste un Dragon."
                jump armar_ejercito
            "Arquero":
                $ unidad = Arquero("Arquero", 120, 25, 12, 4, 4, 30, px, py, 0, True, 30, 10)
                $ ejercito.append(unidad)
                "Agregaste un Arquero."
                jump armar_ejercito
            "Clerigo":
                $ unidad = Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, px, py, 0, True, 100)
                $ ejercito.append(unidad)
                "Agregaste un Clerigo."
                jump armar_ejercito
            "Lich":
                $ unidad = Lich("Lich", 180, 28, 20, 3, 2, 45, px, py, 0, True, 200)
                $ ejercito.append(unidad)
                "Agregaste un Lich."
                jump armar_ejercito
            "Terminar de armar ejercito":
                if total == 0:
                    "No tenes unidades, selecciona al menos una!"
                    jump armar_ejercito
                else:
                    jump elegir_nivel

label elegir_nivel:
    menu:
        "Elegi un nivel:"
        "Nivel 1 - LA INVASION DE LOS GOBLINS":
            jump nivel1
        "Nivel 2 - LA CRIPTA OLVIDADA":
            jump nivel2
        "Nivel 3 - EL BOSQUE DE LAS SOMBRAS":
            jump nivel3
        "Nivel 4 - EL TEMPLO DE LOS CAIDOS":
            jump nivel4
        "Nivel 5 - LA FORTALEZA DEL GENERAL":
            jump nivel5
        "Nivel 6 - EL ABISMO DE LOS CONDENADOS":
            jump nivel6
        "Nivel 7 - EL TRONO DEL SENOR OSCURO":
            jump nivel7
        "Nivel Aleatorio":
            jump nivel_aleatorio

# ============================================================
# ARMAR EJERCITO J1 (VERSUS)
# ============================================================
label armar_ejercito_j1:
    $ total = len(ejercito_j1)

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (3, 4)]
        casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito_j1]
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        if not casillas_disponibles:
            casillas_disponibles = [(0, 4)]
        px, py = random.choice(casillas_disponibles)

    if total >= maxima_cantidad_unidades:
        "Jugador 1 tiene [maxima_cantidad_unidades] unidades. Turno del Jugador 2."
        jump armar_ejercito_j2
    else:
        menu:
            "JUGADOR 1 - Elegi una unidad ([total]/[maxima_cantidad_unidades]):"
            "Mago":
                $ ejercito_j1.append(Mago("J1_Mago", 200, 25, 15, 4, 3, 30, px, py, 0, True, 100, 100, 10, 10, 10))
                jump armar_ejercito_j1
            "Guerrero":
                $ ejercito_j1.append(Guerrero("J1_Guerrero", 150, 40, 20, 4, 1, 35, px, py, 0, True))
                jump armar_ejercito_j1
            "Arquero":
                $ ejercito_j1.append(Arquero("J1_Arquero", 120, 25, 12, 4, 4, 30, px, py, 0, True, 30, 10))
                jump armar_ejercito_j1
            "Dragon":
                $ ejercito_j1.append(Dragon("J1_Dragon", 300, 60, 30, 2, 3, 70, px, py, 0, True, 500, 0, 0))
                jump armar_ejercito_j1
            "Terminar":
                if total == 0:
                    "Elegi al menos una unidad!"
                    jump armar_ejercito_j1
                else:
                    jump armar_ejercito_j2

# ============================================================
# ARMAR EJERCITO J2 (VERSUS)
# ============================================================
label armar_ejercito_j2:
    $ total = len(ejercito_j2)

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (0, 1)]
        casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito_j2]
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        if not casillas_disponibles:
            casillas_disponibles = [(0, 0)]
        px, py = random.choice(casillas_disponibles)

    if total >= maxima_cantidad_unidades:
        "Jugador 2 tiene [maxima_cantidad_unidades] unidades. Empieza la batalla!"
        jump versus_inicio_batalla
    else:
        menu:
            "JUGADOR 2 - Elegi una unidad ([total]/[maxima_cantidad_unidades]):"
            "Mago":
                $ ejercito_j2.append(Mago("J2_Mago", 200, 25, 15, 4, 3, 30, px, py, 0, True, 100, 100, 10, 10, 10))
                jump armar_ejercito_j2
            "Guerrero":
                $ ejercito_j2.append(Guerrero("J2_Guerrero", 150, 40, 20, 4, 1, 35, px, py, 0, True))
                jump armar_ejercito_j2
            "Arquero":
                $ ejercito_j2.append(Arquero("J2_Arquero", 120, 25, 12, 4, 4, 30, px, py, 0, True, 30, 10))
                jump armar_ejercito_j2
            "Dragon":
                $ ejercito_j2.append(Dragon("J2_Dragon", 300, 60, 30, 2, 3, 70, px, py, 0, True, 500, 0, 0))
                jump armar_ejercito_j2
            "Terminar":
                if total == 0:
                    "Elegi al menos una unidad!"
                    jump armar_ejercito_j2
                else:
                    jump versus_inicio_batalla

# ============================================================
# VERSUS
# ============================================================
label versus_inicio:
    $ modo_versus = True
    $ ejercito_j1 = []
    $ ejercito_j2 = []
    "MODO VERSUS - 2 JUGADORES"
    "Jugador 1: Elegi tu ejercito"
    jump armar_ejercito_j1

label versus_inicio_batalla:
    $ turno_actual = 1
    $ texto_turno = "Turno Jugador 1"
    $ unidad_seleccionada = None
    $ partida_terminada = False
    $ resultado_batalla = ""
    "Empieza la batalla!"
    call screen tablero_versus

    if resultado_batalla == "j1_gana":
        jump versus_j1_gana
    elif resultado_batalla == "j2_gana":
        jump versus_j2_gana
    else:
        $ renpy.full_restart()

label versus_j1_gana:
    "JUGADOR 1 GANA!"
    $ renpy.full_restart()

label versus_j2_gana:
    "JUGADOR 2 GANA!"
    $ renpy.full_restart()

# ============================================================
# COMENZAR BATALLA
# ============================================================
label comenzar_batalla:
    "Tu ejercito esta listo!"
    "Mision: Elimina a todos los enemigos del tablero!"
    $ partida_terminada = False
    $ resultado_batalla = ""
    $ boss_spawneado = False
    call screen tablero

    if resultado_batalla == "victoria":
        jump victoria_jugador
    elif resultado_batalla == "derrota":
        jump derrotado
    else:
        $ renpy.full_restart()

# ============================================================
# VICTORIA
# ============================================================
label victoria_jugador:
    $ guardar_partida("partida")

    if nivel_actual == 1:
        call dialogo_nivel1_victoria
    elif nivel_actual == 2:
        call dialogo_nivel2_victoria
    elif nivel_actual == 3:
        call dialogo_nivel3_victoria
    elif nivel_actual == 4:
        call dialogo_nivel4_victoria
    elif nivel_actual == 5:
        call dialogo_nivel5_victoria
    elif nivel_actual == 6:
        call dialogo_nivel6_victoria
    elif nivel_actual == 7:
        call dialogo_nivel7_victoria
        "HAS COMPLETADO EL JUEGO!"
        jump menu_principal
    else:
        "Nivel completado!"

    if nivel_actual >= 1 and nivel_actual <= 6:
        $ siguiente = nivel_actual + 1
        menu:
            "Que queres hacer?"
            "Siguiente Nivel ([siguiente])":
                $ nivel_actual = siguiente
                $ renpy.jump("nivel" + str(nivel_actual))
            "Reiniciar este Nivel":
                $ renpy.jump("nivel" + str(nivel_actual))
            "Rearmar Ejercito":
                jump armar_ejercito
            "Salir al menu":
                $ renpy.full_restart()
    else:
        menu:
            "Que queres hacer?"
            "Rearmar Ejercito":
                jump armar_ejercito
            "Salir al menu":
                $ renpy.full_restart()

label derrotado:
    "GAME OVER. Tus heroes han caido."
    menu:
        "Que queres hacer?"
        "Reiniciar este Nivel":
            $ renpy.jump("nivel" + str(nivel_actual))
        "Rearmar Ejercito":
            jump armar_ejercito
        "Salir al menu":
            $ renpy.full_restart()

label reiniciar_partida:
    $ ejercito = []
    $ enemigos = []
    $ heroe_actual = None
    $ unidad_seleccionada = None
    $ turno_jugador = True
    $ texto_turno = "Tu turno"
    $ partida_terminada = False
    $ resultado_batalla = ""
    $ modo_versus = False
    $ ejercito_j1 = []
    $ ejercito_j2 = []
    jump inicio

# ============================================================
# SCREEN: TABLERO
# ============================================================
screen tablero():
    modal True
    fixed:
        add "tablero.png":
            xsize 1920
            ysize 1080

        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                button:
                    xpos OFFSET_X + columna * CASILLA_W
                    ypos OFFSET_Y + fila * CASILLA_H
                    xsize CASILLA_W
                    ysize CASILLA_H
                    background None
                    action Function(click_casilla, columna, fila)

        for unidad in enemigos:
            if unidad.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add obtener_imagen_enemigo(unidad.get_clase())

        for heroe in heroes:
            if heroe.get_visible():
                if unidad_seleccionada == heroe:
                    add Solid("#FFFF0066"):
                        xpos OFFSET_X + heroe.get_x() * CASILLA_W
                        ypos OFFSET_Y + heroe.get_y() * CASILLA_H
                        xsize CASILLA_W
                        ysize CASILLA_H
                frame:
                    xpos OFFSET_X + heroe.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + heroe.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add {"Kazuki": "Kazuki.png", "Lyra": "Lyra.png", "Gromm": "Gromm.png"}.get(heroe.get_clase(), "default.png")

        for unidad_ejercito in ejercito:
            if unidad_ejercito.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad_ejercito.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad_ejercito.get_y() * CASILLA_H + 25
                    xsize 56
                    ysize 56
                    add obtener_imagen_enemigo(unidad_ejercito.get_clase())

        frame:
            xpos 20
            ypos 20
            background "#00000088"
            text texto_turno:
                size 30

        textbutton "GUARDAR":
            xpos 1700
            ypos 20
            text_size 25
            action Function(guardar_partida, "partida")

        timer 0.5 repeat True action If(partida_terminada, Return("fin"), NullAction())

    key "K_ESCAPE" action [Hide("tablero"), Jump("menu_principal")]

# ============================================================
# SCREEN: TABLERO VERSUS
# ============================================================
screen tablero_versus():
    modal True
    fixed:
        add "tablero.png":
            xsize 1920
            ysize 1080

        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                button:
                    xpos OFFSET_X + columna * CASILLA_W
                    ypos OFFSET_Y + fila * CASILLA_H
                    xsize CASILLA_W
                    ysize CASILLA_H
                    background None
                    action Function(click_casilla_versus, columna, fila)

        for unidad in ejercito_j2:
            if unidad.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add obtener_imagen_enemigo(unidad.get_clase())

        for unidad in ejercito_j1:
            if unidad.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add obtener_imagen_enemigo(unidad.get_clase())

        frame:
            xpos 20
            ypos 20
            background "#00000088"
            text texto_turno:
                size 30

        timer 0.5 repeat True action If(partida_terminada, Return("fin"), NullAction())

    key "K_ESCAPE" action [Hide("tablero_versus"), Jump("menu_principal")]

# ============================================================
# SCREEN: SELECCION DE HEROES
# ============================================================
screen seleccion_heroes():
    add "seleccion_heroe.png"
    modal True
    viewport:
        null

    if seleccion_heroe:
        vbox:
            imagebutton:
                id "Kazuki"
                idle "kasuki_idle.png"
                hover "kasuki_hover.png"
                focus_mask True
                action [SetVariable("heroe_actual", heroes[0]), Return()]

    if seleccion_heroe:
        vbox:
            imagebutton:
                id "Lyra"
                idle "elfa_idle.png"
                hover "elfa_hover.png"
                focus_mask True
                action [SetVariable("heroe_actual", heroes[1]), Return()]

    if seleccion_heroe:
        vbox:
            imagebutton:
                id "Gromm"
                idle "enano_idle.png"
                hover "enano_hover.png"
                focus_mask True
                action [SetVariable("heroe_actual", heroes[2]), Return()]

# ============================================================
# SPLASHSCREEN
# ============================================================
label splashscreen:
    scene black
    with Pause(0.5)
    return

# ============================================================
# LABEL START
# ============================================================
label start:
    jump inicio

label inicio:
    scene black
    python:
        try:
            reproducir_musica("main.wav", fadein=1.0, loop=True)
        except:
            pass
    $ heroes = crear_heroes()
    $ enemigos = []
    "Bienvenido a RE: MERCENARY - Estrategia por turnos"
    call screen seleccion_heroes

    python:
        for h in heroes:
            if h != heroe_actual:
                h.set_visible(False)

    "Has elegido a [heroe_actual.get_clase()]."
    "Ahora arma tu ejercito!"
    jump armar_ejercito

# ============================================================
# LABEL MENU PRINCIPAL
# ============================================================
label menu_principal:
    $ renpy.full_restart()