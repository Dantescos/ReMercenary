# ============================================================
# RE: MERCENARY - SCRIPT PRINCIPAL
# ============================================================

# VARIABLES GLOBALES
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
default seleccion_heroe=True
default slot_guardado = "partida"
default boss_musica_activada = False

# VARIABLES MODO VERSUS
default modo_versus = False
default ejercito_j1 = []
default ejercito_j2 = []
default turno_actual = 1

# Imágenes
image pantalla_inicio = "pantalla_inicio.png"
image portada = "portada.png"

# ============================================================
# CONFIGURACIÓN DEL TABLERO
# ============================================================
init python:
    import random
    COLUMNAS = 8
    FILAS = 5
    OFFSET_X = 180
    OFFSET_Y = 140
    CASILLA_W = 195
    CASILLA_H = 170

# ============================================================
# FUNCIONES DE DAÑO Y STATS
# ============================================================
init python:
    def get_stats_personaje(personaje):
        clase = personaje.get_clase()
        hp = personaje.get_vida()
        texto = "HP: " + str(hp)
        try:
            if clase in ["Kazuki", "Mago", "Archimago", "Lich", "Clerigo", "Dragon", "Mago2", "Lich2", "Archimago2", "Clerigo2"]:
                texto += " | MAGIA: " + str(personaje.get_magia())
            elif clase in ["Lyra", "Arquero", "Arquero2"]:
                texto += " | FLECHAS: " + str(personaje.get_carcaj()) + " | ESP: " + str(personaje.get_flecha_trucada())
            elif clase in ["General", "General2"]:
                texto += " | ENERGIA: " + str(personaje.get_energia())
            elif clase in ["Guerrero", "Gromm", "Guerrero2"]:
                texto += " | (Fisico)"
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
# MOVIMIENTO DE ENEMIGOS
# ============================================================
init python:
    def mover_enemigos():
        heroe = store.heroe_actual
        if heroe is None or not heroe.esta_vivo():
            return
        for enemigo in store.enemigos[:]:
            if not enemigo.get_visible() or not enemigo.esta_vivo():
                continue
            if enemigo.get_x() < heroe.get_x():
                enemigo.set_x(enemigo.get_x() + 1)
            elif enemigo.get_x() > heroe.get_x():
                enemigo.set_x(enemigo.get_x() - 1)
            elif enemigo.get_y() < heroe.get_y():
                enemigo.set_y(enemigo.get_y() + 1)
            elif enemigo.get_y() > heroe.get_y():
                enemigo.set_y(enemigo.get_y() - 1)
            if enemigo.get_x() == heroe.get_x() and enemigo.get_y() == heroe.get_y():
                renpy.call_in_new_context("combate", heroe, enemigo)
                return

# ============================================================
# CREAR HEROES Y ENEMIGOS
# ============================================================
init python:
    def crear_heroes():
        return [Kazuki(2, 3), Lyra(4, 3), Gromm(6, 3)]

    def crear_enemigos():
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        enemigos = []
        x, y = posiciones.pop()
        enemigos.append(Mago("Mago", 200, 25, 15, 4, 3, 30, x, y, 0, True, 100, 10, 10, 10))
        x, y = posiciones.pop()
        enemigos.append(General("General", 250, 30, 20, 3, 2, 40, x, y, 0, True, 1000, 500))
        x, y = posiciones.pop()
        enemigos.append(Arquero("Arquero", 120, 25, 12, 4, 4, 30, x, y, 0, True, 30, 10))
        x, y = posiciones.pop()
        enemigos.append(Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, x, y, 0, True, 100))
        x, y = posiciones.pop()
        enemigos.append(Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, x, y, 0, True))
        x, y = posiciones.pop()
        enemigos.append(Dragon("Dragon", 300, 60, 30, 2, 3, 70, x, y, 0, True, 500, 0, 0))
        x, y = posiciones.pop()
        enemigos.append(Lich("Lich", 180, 28, 20, 3, 2, 45, x, y, 0, True, 200))
        x, y = posiciones.pop()
        enemigos.append(ArchiMago("Archimago", 300, 35, 25, 3, 3, 50, x, y, 0, True, 1500, 100))
        x, y = posiciones.pop()
        enemigos.append(Mago("Mago2", 200, 25, 15, 4, 3, 30, x, y, 0, True, 100, 10, 10, 10))
        x, y = posiciones.pop()
        enemigos.append(General("General2", 250, 30, 20, 3, 2, 40, x, y, 0, True, 1000, 500))
        x, y = posiciones.pop()
        enemigos.append(Arquero("Arquero2", 120, 25, 12, 4, 4, 30, x, y, 0, True, 30, 10))
        x, y = posiciones.pop()
        enemigos.append(Clerigo("Clerigo2", 150, 15, 18, 3, 2, 20, x, y, 0, True, 100))
        x, y = posiciones.pop()
        enemigos.append(Guerrero("Guerrero2", 150, 40, 20, 4, 1, 35, x, y, 0, True))
        x, y = posiciones.pop()
        enemigos.append(Dragon("Dragon2", 300, 60, 30, 2, 3, 70, x, y, 0, True, 500, 0, 0))
        x, y = posiciones.pop()
        enemigos.append(Lich("Lich2", 180, 28, 20, 3, 2, 45, x, y, 0, True, 200))
        x, y = posiciones.pop()
        enemigos.append(ArchiMago("Archimago2", 300, 35, 25, 3, 3, 50, x, y, 0, True, 1500, 100))
        return enemigos

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
init python:
    def quedan_enemigos_vivos():
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo():
                return True
        return False

    def quedan_heroes_vivos():
        for heroe in store.heroes:
            if heroe.get_visible() and heroe.esta_vivo():
                return True
        return False

    def hay_unidades_vivas(ejercito):
        for unidad in ejercito:
            if unidad.get_visible() and unidad.esta_vivo():
                return True
        return False

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

# ============================================================
# CLICK EN CASILLA (MODO NORMAL)
# ============================================================
init python:
    def click_casilla(x, y):
        if not store.turno_jugador:
            renpy.notify("Turno enemigo")
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

        renpy.notify("Turno enemigo")
        store.turno_jugador = False
        store.texto_turno = "Turno enemigo"
        mover_enemigos()

        enemigos_vivos = [e for e in store.enemigos if e.get_visible() and e.esta_vivo()]
        if len(enemigos_vivos) == 1 and not store.boss_musica_activada:
            if store.nivel_actual >= 1 and store.nivel_actual <= 7:
                store.boss_musica_activada = True
                try:
                    reproducir_musica("Boss" + str(store.nivel_actual) + ".wav", fadein=0.5, loop=True)
                    renpy.notify("¡BOSS! ¡Queda 1 enemigo!")
                except:
                    pass

        if not quedan_enemigos_vivos():
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

# ============================================================
# CLICK EN CASILLA (MODO VERSUS)
# ============================================================
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
# COMBATE (MODO NORMAL) - MENÚS COMPLETOS
# ============================================================
label combate(heroe, enemigo):
    python:
        ia = None
        clase_enemigo = enemigo.get_clase()
        if "Archimago" in clase_enemigo:
            ia = IA_ArchiMago()
        elif "Lich" in clase_enemigo:
            ia = IA_Lich()
        elif "Clerigo" in clase_enemigo:
            ia = IA_Clerigo()
        elif "Guerrero" in clase_enemigo:
            ia = IA_Guerrero()
        elif "Arquero" in clase_enemigo:
            ia = IA_Arquero()
        elif "Dragon" in clase_enemigo:
            ia = IA_Dragon()
        elif "Mago" in clase_enemigo:
            ia = IA_Mago()
        elif "General" in clase_enemigo:
            ia = IA_General()
        else:
            ia = None

    while heroe.esta_vivo() and enemigo.esta_vivo():
        $ stats_heroe = get_stats_personaje(heroe)
        $ hp_enemigo = enemigo.get_vida()
        $ nombre_enemigo = enemigo.get_clase()
        $ def_enemiga = enemigo.get_defensa()
        "[stats_heroe]  ||  [nombre_enemigo] HP: [hp_enemigo] (DEF [def_enemiga])"

        $ clase = heroe.get_clase()

        # ============================================
        # KAZUKI (Mago + potenciar) - 10 opciones
        # ============================================
        if clase == "Kazuki":
            menu:
                "Kazuki - ¿Que haras?"
                "Atacar (Bola de Fuego)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.5)
                    $ registrar_habilidad_usada()
                    "¡BOLA DE FUEGO! [danio] de danio."
                "Potenciar aliado (+20%% ATQ)":
                    $ heroe.potenciar_aliado(heroe)
                    $ registrar_habilidad_usada()
                    "¡Kazuki se potencia! ATQ: [heroe.get_ataque_basico()]"
                "Bola de Fuego Mejorada":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.8)
                    $ registrar_habilidad_usada()
                    "¡Bola Mejorada! [danio] de danio."
                "Ataque Hielo Infernal":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.6)
                    $ registrar_habilidad_usada()
                    "¡Hielo Infernal! [danio] de danio."
                "Castigo Divino":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ registrar_habilidad_usada()
                    "¡Castigo Divino! [danio] de danio."
                "Vientos Infernales Prohibidos":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ registrar_habilidad_usada()
                    "¡Vientos Infernales! [danio] de danio."
                "Ataque Magico Prohibido (Waldgose)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.5)
                    $ registrar_habilidad_usada()
                    "¡WALDGOSE! [danio] de danio."
                "Proteccion Magica (+DEF x2)":
                    $ heroe.set_defensa(heroe.get_defensa() * 2)
                    $ registrar_habilidad_usada()
                    "DEF: [heroe.get_defensa()]"
                "Curacion Magica":
                    $ heroe.set_vida(min(heroe.get_vida() + 50, 180))
                    $ registrar_habilidad_usada()
                    "HP: [heroe.get_vida()]"
                "Recuperar Magia":
                    $ heroe.set_magia(min(heroe.get_magia() + 100, 250))
                    "MAGIA: [heroe.get_magia()]"
                "Magia de Vuelo (5 casillas)":
                    $ heroe.set_magia(max(0, heroe.get_magia() - 30))
                    $ registrar_habilidad_usada()
                    "¡Teletransporte! MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # LYRA (Arquero + flecha_perforante) - 9 opciones
        # ============================================
        elif clase == "Lyra":
            menu:
                "Lyra - ¿Que haras?"
                "Disparar Flecha":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    "Disparas. [danio] de danio. Flechas: [heroe.get_carcaj()]"
                "Flecha Perforante":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.8)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    $ registrar_habilidad_usada()
                    "¡PERFORANTE! [danio] de danio."
                "Flecha de Hielo":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    $ registrar_habilidad_usada()
                    "¡Flecha de Hielo! [danio] de danio."
                "Flecha Venenosa":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    $ registrar_habilidad_usada()
                    "¡Venenosa! [danio] de danio."
                "Flecha Explosiva":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.0)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    $ registrar_habilidad_usada()
                    "¡EXPLOSIVA! [danio] de danio."
                "Flecha Electrica":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.5)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    $ registrar_habilidad_usada()
                    "¡Electrica! [danio] de danio."
                "Tiro Doble":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.2)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 2))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 2))
                    $ registrar_habilidad_usada()
                    "¡Tiro Doble! [danio] de danio."
                "Recargar Carcaj":
                    $ heroe.set_carcaj(30)
                    $ heroe.set_flecha_trucada(10)
                    "Recargas. Flechas: [heroe.get_carcaj()] Esp: [heroe.get_flecha_trucada()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # GROMM (Guerrero + escudo) - 4 opciones
        # ============================================
        elif clase == "Gromm":
            menu:
                "Gromm - ¿Que haras?"
                "Atacar":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    "¡Golpe! [danio] de danio."
                "Testudo (+DEF x2)":
                    $ heroe.testudo()
                    $ registrar_habilidad_usada()
                    "DEF: [heroe.get_defensa()]"
                "Arremeter (+20 ATQ)":
                    $ heroe.arremeter()
                    $ registrar_habilidad_usada()
                    "ATQ: [heroe.get_ataque_basico()]"
                "Escudo Levantado (+DEF x2)":
                    $ heroe.escudo_levantado()
                    $ registrar_habilidad_usada()
                    "DEF: [heroe.get_defensa()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # MAGO generico - 10 opciones
        # ============================================
        elif clase == "Mago" or clase == "Mago2":
            menu:
                "Mago - ¿Que haras?"
                "Atacar (Ragnarok)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.5)
                    $ registrar_habilidad_usada()
                    "¡Ragnarok! [danio] de danio."
                "Bola de Fuego Mejorada":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.8)
                    $ registrar_habilidad_usada()
                    "¡Bola! [danio] de danio."
                "Ataque Hielo Infernal":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.6)
                    $ registrar_habilidad_usada()
                    "¡Hielo! [danio] de danio."
                "Castigo Divino":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ registrar_habilidad_usada()
                    "¡Castigo! [danio] de danio."
                "Vientos Infernales":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ registrar_habilidad_usada()
                    "¡Vientos! [danio] de danio."
                "Ataque Prohibido (Waldgose)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.5)
                    $ registrar_habilidad_usada()
                    "¡WALDGOSE! [danio] de danio."
                "Proteccion Magica":
                    $ heroe.set_defensa(heroe.get_defensa() * 2)
                    "DEF: [heroe.get_defensa()]"
                "Curacion Magica":
                    $ heroe.set_vida(min(heroe.get_vida() + 50, 200))
                    "HP: [heroe.get_vida()]"
                "Recuperar Magia":
                    $ heroe.set_magia(min(heroe.get_magia() + 100, 1000))
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # ARCHIMAGO - 13 opciones
        # ============================================
        elif clase == "Archimago" or clase == "Archimago2":
            menu:
                "Archimago - ¿Que haras?"
                "Atacar (Vollzanbel)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.5)
                    "¡Vollzanbel! [danio] de danio."
                "Doom":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ registrar_habilidad_usada()
                    "¡DOOM! [danio] de danio."
                "Ataque Gelido (Todlicher Winter)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.8)
                    $ registrar_habilidad_usada()
                    "¡Todlicher Winter! [danio] de danio."
                "Ataque Oscuro (Ewige Finsternis)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.2)
                    $ registrar_habilidad_usada()
                    "¡Ewige Finsternis! [danio] de danio."
                "Espadas de Luz (Catastravia)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ registrar_habilidad_usada()
                    "¡Catastravia! [danio] de danio."
                "Relampago (Judradjim)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.8)
                    $ registrar_habilidad_usada()
                    "¡Judradjim! [danio] de danio."
                "Ataque Final (Zooltraak 10x)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 10.0)
                    $ registrar_habilidad_usada()
                    "¡ZOOLTRAAK! [danio] de danio."
                "Sabiduria Ancestral (+300 Magia)":
                    $ heroe.set_magia(min(heroe.get_magia() + 300, 1500))
                    "MAGIA: [heroe.get_magia()]"
                "Detener el Tiempo":
                    $ heroe.set_magia(max(0, heroe.get_magia() - 200))
                    $ registrar_habilidad_usada()
                    "¡TIEMPO DETENIDO! MAGIA: [heroe.get_magia()]"
                "Ilusion de Archimago":
                    $ heroe.set_magia(max(0, heroe.get_magia() - 100))
                    "Ilusion activada."
                "Curacion Magica":
                    $ heroe.set_vida(min(heroe.get_vida() + 50, 300))
                    "HP: [heroe.get_vida()]"
                "Recuperar Magia":
                    $ heroe.set_magia(min(heroe.get_magia() + 200, 1500))
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # GUERRERO generico - 3 opciones
        # ============================================
        elif clase == "Guerrero" or clase == "Guerrero2":
            menu:
                "Guerrero - ¿Que haras?"
                "Atacar":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    "Atacas. [danio] de danio."
                "Testudo (+DEF x2)":
                    $ heroe.testudo()
                    "DEF: [heroe.get_defensa()]"
                "Arremeter (+20 ATQ)":
                    $ heroe.arremeter()
                    "ATQ: [heroe.get_ataque_basico()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # ARQUERO generico - 8 opciones
        # ============================================
        elif clase == "Arquero" or clase == "Arquero2":
            menu:
                "Arquero - ¿Que haras?"
                "Disparar Flecha":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    "Disparas. [danio] de danio. Flechas: [heroe.get_carcaj()]"
                "Flecha Especial":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.8)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 1))
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    "¡Especial! [danio] de danio."
                "Flecha de Hielo":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    "¡Hielo! [danio] de danio."
                "Flecha Venenosa":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    "¡Venenosa! [danio] de danio."
                "Flecha Explosiva":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.0)
                    $ heroe.set_flecha_trucada(max(0, heroe.get_flecha_trucada() - 1))
                    "¡Explosiva! [danio] de danio."
                "Tiro Doble":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.2)
                    $ heroe.set_carcaj(max(0, heroe.get_carcaj() - 2))
                    "¡Tiro Doble! [danio] de danio."
                "Recargar":
                    $ heroe.set_carcaj(30)
                    $ heroe.set_flecha_trucada(10)
                    "Recargas. Flechas: [heroe.get_carcaj()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # LICH - 6 opciones
        # ============================================
        elif clase == "Lich" or clase == "Lich2":
            menu:
                "Lich - ¿Que haras?"
                "Orbe de Sombras":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.5)
                    "¡Orbe! [danio] de danio."
                "Ataque Espectral":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.8)
                    $ registrar_habilidad_usada()
                    "¡Espectral! [danio] de danio."
                "Drenar Vida":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ heroe.set_vida(min(heroe.get_vida() + danio // 2, 180))
                    $ registrar_habilidad_usada()
                    "¡Drenar! [danio] de danio. HP: [heroe.get_vida()]"
                "Ataque Masivo":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.0)
                    $ registrar_habilidad_usada()
                    "¡Masivo! [danio] de danio."
                "Curar":
                    $ heroe.set_vida(min(heroe.get_vida() + 50, 180))
                    "HP: [heroe.get_vida()]"
                "Regenerar Magia":
                    $ heroe.set_magia(min(heroe.get_magia() + 50, 200))
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # CLERIGO - 7 opciones
        # ============================================
        elif clase == "Clerigo" or clase == "Clerigo2":
            menu:
                "Clerigo - ¿Que haras?"
                "Bendicion Sangrada":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.5)
                    "¡Bendicion! [danio] de danio."
                "Luz Cegadora del Dia":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ registrar_habilidad_usada()
                    "¡Luz! [danio] de danio."
                "Exorcismo":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 3.5)
                    $ registrar_habilidad_usada()
                    "¡EXORCISMO! [danio] de danio."
                "Palabras de Fe (reduce ATQ)":
                    $ enemigo.set_ataque_basico(int(enemigo.get_ataque_basico() * 0.6))
                    $ registrar_habilidad_usada()
                    "ATQ enemigo reducido a [enemigo.get_ataque_basico()]"
                "Escudo de Fe (+1000 DEF)":
                    $ heroe.set_defensa(heroe.get_defensa() + 1000)
                    $ registrar_habilidad_usada()
                    "DEF: [heroe.get_defensa()]"
                "Mi Fe es Inquebrantable (10x)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 10.0)
                    $ registrar_habilidad_usada()
                    "¡FE INQUEBRANTABLE! [danio] de danio."
                "Recuperar Magia":
                    $ heroe.set_magia(min(heroe.get_magia() + 200, 1000))
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # GENERAL - 7 opciones
        # ============================================
        elif clase == "General" or clase == "General2":
            menu:
                "General - ¿Que haras?"
                "Espada (Corte Mortal)":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    "¡Corte! [danio] de danio."
                "Canon de Mano":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ registrar_habilidad_usada()
                    "¡Canon! [danio] de danio."
                "Tiro Doble":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.5)
                    $ registrar_habilidad_usada()
                    "¡Tiro Doble! [danio] de danio."
                "Carga de Caballeria":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ registrar_habilidad_usada()
                    "¡Carga! [danio] de danio."
                "Canon Final (10x)":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 10.0)
                    $ registrar_habilidad_usada()
                    "¡CAÑON FINAL! [danio] de danio."
                "Potenciador Cercano (+ATQ aliado)":
                    $ registrar_habilidad_usada()
                    "¡Aliados potenciados! ATQ: [heroe.get_ataque_basico()]"
                "Potenciador Lejano":
                    $ registrar_habilidad_usada()
                    "Potenciador a distancia activado."
                "Huir":
                    "Escapaste!"
                    return

        # ============================================
        # DRAGON - 8 opciones
        # ============================================
        elif clase == "Dragon" or clase == "Dragon2":
            menu:
                "Dragon - ¿Que haras?"
                "Golpe Draconico":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    "¡Golpe! [danio] de danio."
                "Llamarada Infernal":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.0)
                    $ registrar_habilidad_usada()
                    "¡Llamarada! [danio] de danio."
                "Ataque de Espinas":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 1.5)
                    $ registrar_habilidad_usada()
                    "¡Espinas! [danio] de danio."
                "Rayo de Luz":
                    $ danio = aplicar_danio_magico(heroe, enemigo, 2.2)
                    $ registrar_habilidad_usada()
                    "¡Rayo de Luz! [danio] de danio."
                "Escamas Reflectantes":
                    $ registrar_habilidad_usada()
                    "¡Escamas activadas por 2 turnos!"
                "Regeneracion":
                    $ heroe.set_vida(min(heroe.get_vida() + 30, 450))
                    "HP: [heroe.get_vida()]"
                "Recuperar Magia":
                    $ heroe.set_magia(min(heroe.get_magia() + 100, 500))
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    "Escapaste!"
                    return

        # FALLBACK
        else:
            menu:
                "[clase] - ¿Que haras?"
                "Atacar":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    "Atacas. [danio] de danio."
                "Huir":
                    "Escapaste!"
                    return

        if not enemigo.esta_vivo():
            "¡[nombre_enemigo] HA SIDO DERROTADO!"
            $ enemigo.set_visible(False)
            $ registrar_muerte_enemigo()
            return

        python:
            if ia is not None:
                try:
                    if "Clerigo" in enemigo.get_clase():
                        ia.evaluar(enemigo, heroe, store.enemigos)
                    else:
                        ia.evaluar(enemigo, heroe)
                except Exception as e:
                    danio_enemigo = max(5, enemigo.get_ataque_basico() // 2)
                    heroe.set_vida(max(0, heroe.get_vida() - danio_enemigo))
                    renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")
            else:
                danio_enemigo = max(5, enemigo.get_ataque_basico() // 2)
                heroe.set_vida(max(0, heroe.get_vida() - danio_enemigo))
                renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")

        if not heroe.esta_vivo():
            $ nombre_heroe_muerto = heroe.get_clase()
            "¡[nombre_heroe_muerto] HA CAIDO!"
            $ heroe.set_visible(False)
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
# ARMAR EJERCITO (MODO NORMAL)
# ============================================================
label armar_ejercito:
    $ total = len(ejercito)
    if total >= maxima_cantidad_unidades:
        "Ya tenes [maxima_cantidad_unidades] unidades. No podes agregar mas!"
        jump comenzar_batalla

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (3, 4)]
        casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito]
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        if not casillas_disponibles:
            casillas_disponibles = [(0, 4)]
        px, py = random.choice(casillas_disponibles)

    menu:
        "Elegi una unidad para tu ejercito ([total]/[maxima_cantidad_unidades]):"
        "Mago":
            $ unidad = Mago("Mago", 200, 25, 15, 4, 3, 30, px, py, 0, True, 100, 10, 10, 10)
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
    if total >= maxima_cantidad_unidades:
        jump armar_ejercito_j2

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (3, 4)]
        casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito_j1]
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        if not casillas_disponibles:
            casillas_disponibles = [(0, 4)]
        px, py = random.choice(casillas_disponibles)

    menu:
        "JUGADOR 1 - Elegi una unidad ([total]/[maxima_cantidad_unidades]):"
        "Mago":
            $ ejercito_j1.append(Mago("J1_Mago", 200, 25, 15, 4, 3, 30, px, py, 0, True, 100, 10, 10, 10))
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
    if total >= maxima_cantidad_unidades:
        jump versus_inicio_batalla

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (0, 1)]
        casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito_j2]
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        if not casillas_disponibles:
            casillas_disponibles = [(0, 0)]
        px, py = random.choice(casillas_disponibles)

    menu:
        "JUGADOR 2 - Elegi una unidad ([total]/[maxima_cantidad_unidades]):"
        "Mago":
            $ ejercito_j2.append(Mago("J2_Mago", 200, 25, 15, 4, 3, 30, px, py, 0, True, 100, 10, 10, 10))
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
    "Jugador 1: Elegi tu ejercito (abajo)"
    jump armar_ejercito_j1

label versus_inicio_batalla:
    $ turno_actual = 1
    $ texto_turno = "Turno Jugador 1"
    $ unidad_seleccionada = None
    $ partida_terminada = False
    $ resultado_batalla = ""
    "¡Empieza la batalla!"
    call screen tablero_versus

    if resultado_batalla == "j1_gana":
        jump versus_j1_gana
    elif resultado_batalla == "j2_gana":
        jump versus_j2_gana
    else:
        $ renpy.full_restart()

label versus_j1_gana:
    "¡JUGADOR 1 GANA!"
    $ renpy.full_restart()

label versus_j2_gana:
    "¡JUGADOR 2 GANA!"
    $ renpy.full_restart()

# ============================================================
# COMENZAR BATALLA (MODO NORMAL)
# ============================================================
label comenzar_batalla:
    "¡Tu ejercito esta listo!"
    "Misión: ¡Elimina a todos los enemigos del tablero!"
    $ partida_terminada = False
    $ resultado_batalla = ""
    call screen tablero

    if resultado_batalla == "victoria":
        jump victoria_jugador
    elif resultado_batalla == "derrota":
        jump derrotado
    else:
        $ renpy.full_restart()

# ============================================================
# VICTORIA - ¡ACÁ ESTÁ EL FIX DE SIGUIENTE NIVEL!
# ============================================================
label victoria_jugador:
    $ guardar_partida("partida")

    # Mostrar diálogo de victoria según nivel
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
        "¡HAS COMPLETADO EL JUEGO!"
        jump menu_principal
    else:
        "¡Nivel completado!"

    # Menú de opciones post-victoria
    if nivel_actual >= 1 and nivel_actual <= 6:
        $ siguiente = nivel_actual + 1
        menu:
            "¿Que queres hacer?"
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
            "¿Que queres hacer?"
            "Rearmar Ejercito":
                jump armar_ejercito
            "Salir al menu":
                $ renpy.full_restart()

label derrotado:
    "GAME OVER. Tus heroes han caido."
    menu:
        "¿Que queres hacer?"
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
                    add {"Dragon": "Dragon.png", "Lich": "Lich.png", "Archimago": "Archimago.png",
                        "Mago": "Mago.png", "Clerigo": "Clerigo.png", "Guerrero": "Guerrero.png",
                        "General": "General.png", "Arquero": "Arquero.png"}.get(unidad.get_clase(), "default.png")

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
                    add {"Dragon": "Dragon.png", "Lich": "Lich.png", "Archimago": "Archimago.png",
                        "Mago": "Mago.png", "Clerigo": "Clerigo.png", "Guerrero": "Guerrero.png",
                        "General": "General.png", "Arquero": "Arquero.png"}.get(unidad_ejercito.get_clase(), "default.png")

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
                    add {"Dragon": "Dragon.png", "Lich": "Lich.png", "Archimago": "Archimago.png",
                        "Mago": "Mago.png", "Clerigo": "Clerigo.png", "Guerrero": "Guerrero.png",
                        "General": "General.png", "Arquero": "Arquero.png"}.get(unidad.get_clase(), "default.png")

        for unidad in ejercito_j1:
            if unidad.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add {"Dragon": "Dragon.png", "Lich": "Lich.png", "Archimago": "Archimago.png",
                        "Mago": "Mago.png", "Clerigo": "Clerigo.png", "Guerrero": "Guerrero.png",
                        "General": "General.png", "Arquero": "Arquero.png"}.get(unidad.get_clase(), "default.png")

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
    $ enemigos = crear_enemigos()
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
