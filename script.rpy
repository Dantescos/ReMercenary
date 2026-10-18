# ============================================================
# RE: MERCENARY - SCRIPT PRINCIPAL (VERSION FINAL CORREGIDA)
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
default tablero_actual = "tablero.png"
default boss_aleatorio_pendiente = False
default combate_versus_atacante = None
default combate_versus_defensor = None
default combate_versus_accion = "idle"
default combate_versus_resultado = ""
default combate_versus_activo = False
default combate_versus_huida = False
default combate_versus_terminado = False
default combate_historia_huida = False
default enemigos_moviendo = False
default enemigos_pendientes = []
default codigo_secreto = ""
default minijuego_activo = False
default goku_x = 340
default goku_y = 540
default goku_vida = 100
default goku_poder = 0
default goku_cargando = False
default goku_accion = "idle"
default goku_frame = 0
default goku_facing = 1
default goku_accion_ticks = 0
default freezer_x = 1540
default freezer_y = 540
default freezer_vida = 100
default freezer_accion = "idle"
default freezer_frame = 0
default freezer_facing = -1
default freezer_cooldown = 0.0
default mini_proyectil_activo = False
default mini_proyectil_x = 0
default mini_proyectil_y = 0
default mini_proyectil_direccion = 1
default mini_resultado = ""
default tipos_unidades_ejercito = ["Mago", "General", "Archimago", "Guerrero", "Dragon", "Arquero", "Clerigo", "Lich", "Sacerdotisa", "Demonia", "Licha"]
default tipos_unidades_versus = ["Mago", "Guerrero", "Arquero", "Dragon", "Sacerdotisa", "Demonia", "Licha"]

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

    def icono_accion_menu(texto):
        texto = texto.lower()
        if any(p in texto for p in ("curar", "curacion", "curación", "vida", "sanar", "beso")):
            return "+"
        if any(p in texto for p in ("defender", "defensa", "proteger", "testudo", "escudo")):
            return "⛨"
        if any(p in texto for p in ("magia", "recuperar", "sabiduria", "sabiduría", "vuelo")):
            return "✦"
        if any(p in texto for p in ("ataque", "atacar", "bola", "fuego", "hielo", "espada", "canon", "cañon", "tiro", "drenar", "latigazo", "castigo", "miasma", "golpe")):
            return "⚔"
        return "•"

    def crear_unidad_ejercito(tipo, x, y, equipo=""):
        nombre = (equipo + "_" + tipo) if equipo else tipo
        if tipo == "Mago":
            return Mago(nombre, 1200, 200, 100, 4, 3, 200, x, y, 0, True, 1500, 1500, 15, 15, 15)
        elif tipo == "General":
            return General(nombre, 1500, 180, 120, 3, 2, 200, x, y, 0, True, 3000, 1000)
        elif tipo == "Archimago":
            return ArchiMago(nombre, 1500, 230, 130, 3, 3, 250, x, y, 0, True, 4000, 300)
        elif tipo == "Guerrero":
            return Guerrero(nombre, 1400, 230, 130, 4, 1, 200, x, y, 0, True)
        elif tipo == "Dragon":
            return Dragon(nombre, 1800, 280, 130, 2, 3, 280, x, y, 0, True, 2500, 0, 0)
        elif tipo == "Arquero":
            return Arquero(nombre, 1000, 200, 90, 4, 4, 230, x, y, 0, True, 80, 30)
        elif tipo == "Clerigo":
            return Clerigo(nombre, 1200, 150, 110, 3, 2, 150, x, y, 0, True, 2000)
        elif tipo == "Lich":
            return Lich(nombre, 1200, 220, 110, 3, 2, 230, x, y, 0, True, 2000)
        elif tipo == "Sacerdotisa":
            return Sacerdotisa(x, y)
        elif tipo == "Demonia":
            return Demonia(x, y)
        elif tipo == "Licha":
            return Licha(x, y)
        return None

    def get_stats_personaje(personaje):
        hp = personaje.get_vida()
        hp_max = personaje.get_vida_max()
        texto = "HP: " + formato_recurso_combate(hp) + "/" + formato_recurso_combate(hp_max)
        try:
            if isinstance(personaje, store.Sacerdotisa):
                texto += " | MAGIA: " + formato_recurso_combate(personaje.get_magia()) + "/" + formato_recurso_combate(personaje.get_magia_max())
            elif isinstance(personaje, store.Demonia):
                texto += " | MAGIA: " + formato_recurso_combate(personaje.get_magia()) + "/" + formato_recurso_combate(personaje.get_magia_max())
            elif isinstance(personaje, store.Licha):
                texto += " | MAGIA: " + formato_recurso_combate(personaje.get_magia()) + "/" + formato_recurso_combate(personaje.get_magia_max()) + " | INVOC: " + str(personaje.get_invocaciones())
            elif isinstance(personaje, (store.Mago, store.ArchiMago, store.Lich, store.Clerigo, store.Dragon)):
                texto += " | MAGIA: " + formato_recurso_combate(personaje.get_magia()) + "/" + formato_recurso_combate(personaje.get_magia_max())
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
        return defensor.defenderse_recibir_danio(atacante.get_ataque_basico())

    def aplicar_danio_magico(atacante, defensor, multiplicador):
        danio = int(atacante.get_ataque_basico() * multiplicador)
        return defensor.defenderse_recibir_danio(danio)

    MINIJUEGO_FRAME_SECUENCIAS = {
        "goku": {
            "punch": (0, 1, 2, 3, 4), "charge": (8,), "blast": (2, 3, 4),
            "right": (0, 1, 2), "left": (0, 2, 3, 4),
            "up": (2, 3, 4), "down": (0, 1, 2, 3, 4),
        },
        "freezer": {
            "punch": (0, 1, 2, 3), "charge": (10,), "blast": (1, 2, 3),
            "right": (0, 1, 3, 4), "left": (0, 1, 4),
            "up": (0, 1, 2, 3, 4, 5), "down": (0, 1, 2, 3, 4),
        },
    }
    MINIJUEGO_CANTIDAD_FRAMES = dict(
        (personaje, dict((accion, len(frames)) for accion, frames in acciones.items()))
        for personaje, acciones in MINIJUEGO_FRAME_SECUENCIAS.items()
    )

    def imagen_minijuego(personaje, accion, frame):
        if accion == "idle":
            accion, frame = "punch", 0
        secuencia = MINIJUEGO_FRAME_SECUENCIAS.get(personaje, {}).get(accion, (0,))
        frame = secuencia[int(frame) % len(secuencia)]
        if accion == "blast":
            frame = MINIJUEGO_FRAME_SECUENCIAS[personaje]["punch"][frame]
            accion = "punch"
        return "images/minijuego/%s_%s_%02d.png" % (personaje, accion, frame)

    def iniciar_minijuego_gkssj():
        store.minijuego_activo = True
        store.goku_x, store.goku_y, store.goku_vida, store.goku_poder = 340, 540, 100, 0
        store.goku_cargando = False
        store.goku_accion, store.goku_frame, store.goku_facing = "idle", 0, 1
        store.goku_accion_ticks = 0
        store.freezer_x, store.freezer_y, store.freezer_vida = 1540, 540, 100
        store.freezer_accion, store.freezer_frame, store.freezer_facing = "idle", 0, -1
        store.freezer_cooldown = 0.0
        store.mini_proyectil_activo = False
        store.mini_resultado = ""

    def minijuego_mover_goku(dx, dy, accion):
        if not store.minijuego_activo or store.goku_cargando:
            return
        store.goku_x = max(130, min(1790, store.goku_x + dx))
        store.goku_y = max(335, min(820, store.goku_y + dy))
        if dx:
            store.goku_facing = 1 if dx > 0 else -1
        store.goku_accion, store.goku_frame = accion, 0
        store.goku_accion_ticks = 5

    def minijuego_toggle_carga():
        if not store.minijuego_activo:
            return
        store.goku_cargando = not store.goku_cargando
        if store.goku_cargando:
            store.goku_accion, store.goku_frame = "charge", 0
        elif store.goku_accion == "charge":
            store.goku_accion, store.goku_frame = "idle", 0

    def minijuego_golpear():
        if not store.minijuego_activo or store.goku_cargando:
            return
        store.goku_accion, store.goku_frame = "punch", 0
        store.goku_accion_ticks = 5
        cerca = abs(store.goku_x - store.freezer_x) <= 145 and abs(store.goku_y - store.freezer_y) <= 105
        frente = (store.freezer_x - store.goku_x) * store.goku_facing >= 0
        if cerca and frente:
            store.freezer_vida = max(0, store.freezer_vida - 18)
            store.mini_resultado = "¡Golpe!"
            minijuego_revisar_fin()
        else:
            store.mini_resultado = "Acércate a Freezer para golpear."

    def minijuego_disparar():
        if not store.minijuego_activo or store.goku_cargando:
            return
        if store.goku_poder < 15:
            store.mini_resultado = "Carga poder con X antes de disparar."
            return
        store.goku_poder -= 15
        store.goku_accion, store.goku_frame = "blast", 0
        store.goku_accion_ticks = 5
        store.mini_proyectil_direccion = store.goku_facing
        store.mini_proyectil_x = store.goku_x + 95 * store.goku_facing
        store.mini_proyectil_y = store.goku_y
        store.mini_proyectil_activo = True
        store.mini_resultado = "¡Kamehameha!"

    def minijuego_revisar_fin():
        if store.freezer_vida <= 0:
            store.minijuego_activo = False
            store.mini_resultado = "¡Goku ganó!"
        elif store.goku_vida <= 0:
            store.minijuego_activo = False
            store.mini_resultado = "Freezer ganó."

    def minijuego_tick():
        if not store.minijuego_activo:
            return

        if store.goku_cargando:
            store.goku_poder = min(100, store.goku_poder + 2)
            store.goku_accion = "charge"

        if store.goku_accion != "idle":
            total = MINIJUEGO_CANTIDAD_FRAMES["goku"].get(store.goku_accion, 1)
            store.goku_frame = (store.goku_frame + 1) % total
            if store.goku_accion_ticks > 0:
                store.goku_accion_ticks -= 1
            elif not store.goku_cargando:
                store.goku_accion, store.goku_frame = "idle", 0

        freezer_total = MINIJUEGO_CANTIDAD_FRAMES["freezer"].get(store.freezer_accion, 1)
        store.freezer_frame = (store.freezer_frame + 1) % freezer_total

        if store.mini_proyectil_activo:
            store.mini_proyectil_x += 38 * store.mini_proyectil_direccion
            if abs(store.mini_proyectil_x - store.freezer_x) < 85 and abs(store.mini_proyectil_y - store.freezer_y) < 125:
                store.freezer_vida = max(0, store.freezer_vida - 24)
                store.mini_proyectil_activo = False
                minijuego_revisar_fin()
            elif not 0 <= store.mini_proyectil_x <= 1920:
                store.mini_proyectil_activo = False

    def minijuego_freezer_tick():
        if not store.minijuego_activo:
            return
        store.freezer_cooldown = max(0.0, store.freezer_cooldown - 0.35)
        dx, dy = store.goku_x - store.freezer_x, store.goku_y - store.freezer_y
        if abs(dx) <= 150 and abs(dy) <= 115:
            if store.freezer_accion != "punch":
                store.freezer_accion, store.freezer_frame = "punch", 0
            if store.freezer_cooldown == 0:
                store.goku_vida = max(0, store.goku_vida - 8)
                store.freezer_cooldown = 1.4
                store.mini_resultado = "Freezer te golpeó."
                minijuego_revisar_fin()
            return
        if dx:
            step_x = min(34, abs(dx)) * (1 if dx > 0 else -1)
            store.freezer_x += step_x
            store.freezer_facing = 1 if step_x > 0 else -1
        if abs(dy) > 36:
            store.freezer_y += min(30, abs(dy) - 36) * (1 if dy > 0 else -1)
        if abs(dx) > abs(dy):
            nueva_accion = "right" if dx > 0 else "left"
        else:
            nueva_accion = "down" if dy > 0 else "up"
        if store.freezer_accion != nueva_accion:
            store.freezer_accion, store.freezer_frame = nueva_accion, 0

# ============================================================
# MOVIMIENTO DE ENEMIGOS
# ============================================================
init python:
    def casillas_ocupadas_por_unidades(unidades, excluir=None):
        ocupadas = set()
        for unidad in unidades:
            if unidad is excluir or not unidad.get_visible() or not unidad.esta_vivo():
                continue
            ocupadas.add((unidad.get_x(), unidad.get_y()))
        return ocupadas

    def reparar_solapamientos_fichas(unidades):
        """Mueve fichas activas que comparten casilla o quedaron fuera del tablero."""
        ocupadas = set()
        for unidad in unidades:
            if not unidad.get_visible() or not unidad.esta_vivo():
                continue

            x, y = unidad.get_x(), unidad.get_y()
            if (x, y) not in ocupadas and 0 <= x < COLUMNAS and 0 <= y < FILAS:
                ocupadas.add((x, y))
                continue

            libres = [
                (cx, cy)
                for cy in range(FILAS)
                for cx in range(COLUMNAS)
                if (cx, cy) not in ocupadas
            ]
            if not libres:
                print("[TABLERO] No hay casillas libres para reubicar " + unidad.get_clase())
                continue

            destino = min(libres, key=lambda p: abs(p[0] - x) + abs(p[1] - y))
            unidad.set_x(destino[0])
            unidad.set_y(destino[1])
            ocupadas.add(destino)
            print("[TABLERO] Ficha reubicada: " + unidad.get_clase() + " -> " + str(destino))

    def casillas_movimiento_historia(unidad):
        if unidad is None:
            return []

        ocupadas = set()
        for otra in store.heroes + store.ejercito + store.enemigos:
            if otra != unidad and otra.get_visible() and otra.esta_vivo():
                ocupadas.add((otra.get_x(), otra.get_y()))

        disponibles = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = unidad.get_x() + dx, unidad.get_y() + dy
            if 0 <= nx < COLUMNAS and 0 <= ny < FILAS and (nx, ny) not in ocupadas:
                disponibles.append((nx, ny))
        return disponibles

    def mover_enemigo(enemigo):
        if enemigo is None or not enemigo.get_visible() or not enemigo.esta_vivo():
            return False

        objetivos = [
            unidad for unidad in store.heroes + store.ejercito
            if unidad.get_visible() and unidad.esta_vivo()
        ]
        if not objetivos:
            return False

        ex, ey = enemigo.get_x(), enemigo.get_y()
        ocupadas = set()
        for otra in store.enemigos + store.heroes + store.ejercito:
            if otra != enemigo and otra.get_visible() and otra.esta_vivo():
                ocupadas.add((otra.get_x(), otra.get_y()))

        # Busca una casilla libre junto al objetivo y rodea obstáculos.
        metas = set()
        for objetivo in objetivos:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                mx, my = objetivo.get_x() + dx, objetivo.get_y() + dy
                if 0 <= mx < COLUMNAS and 0 <= my < FILAS and (mx, my) not in ocupadas:
                    metas.add((mx, my))

        if (ex, ey) in metas:
            return False

        cola = [(ex, ey)]
        padres = {(ex, ey): None}
        destino = None
        while cola and destino is None:
            actual = cola.pop(0)
            if actual in metas:
                destino = actual
                break
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                siguiente = (actual[0] + dx, actual[1] + dy)
                if not (0 <= siguiente[0] < COLUMNAS and 0 <= siguiente[1] < FILAS):
                    continue
                if siguiente in ocupadas or siguiente in padres:
                    continue
                padres[siguiente] = actual
                cola.append(siguiente)

        if destino is None:
            return False

        paso = destino
        while padres[paso] != (ex, ey):
            paso = padres[paso]
        enemigo.set_x(paso[0])
        enemigo.set_y(paso[1])
        print("[MOV] " + enemigo.get_clase() + " -> (" + str(paso[0]) + "," + str(paso[1]) + ")")
        return True

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


# ============================================================
# CLICK EN CASILLA (MODO NORMAL)
# ============================================================
init python:
    def finalizar_turno_historia():
        if not quedan_enemigos_vivos() and not store.boss_spawneado:
            bx, by = 4, 0
            nuevo_boss = None
            if store.nivel_actual >= 1 and store.nivel_actual <= 7:
                nuevo_boss = crear_boss_por_nivel(store.nivel_actual, bx, by)
            elif store.nivel_actual == 0:
                nuevo_boss = crear_boss_aleatorio(bx, by)

            if nuevo_boss is not None:
                store.enemigos.append(nuevo_boss)
                reparar_solapamientos_fichas(store.heroes + store.ejercito + store.enemigos)
                store.boss_spawneado = True
                try:
                    reproducir_musica("Boss" + str(store.nivel_actual) + ".wav", fadein=0.5, loop=True)
                except Exception:
                    pass
                renpy.notify("¡EL BOSS HA APARECIDO!")

        if store.boss_spawneado and not quedan_enemigos_vivos():
            store.resultado_batalla = "victoria"
            store.partida_terminada = True
            store.unidad_seleccionada = None
            return

        if not quedan_heroes_vivos():
            store.resultado_batalla = "derrota"
            store.partida_terminada = True
            store.unidad_seleccionada = None
            return

        store.turno_jugador = True
        store.texto_turno = "Tu turno"
        store.unidad_seleccionada = None
        renpy.notify("Tu turno")

    def mover_siguiente_enemigo_turno():
        if not store.enemigos_moviendo:
            return

        while store.enemigos_pendientes:
            enemigo = store.enemigos_pendientes.pop(0)
            if enemigo.get_visible() and enemigo.esta_vivo():
                mover_enemigo(enemigo)
                break

        if not store.enemigos_pendientes:
            store.enemigos_moviendo = False
            finalizar_turno_historia()

        # El timer y la acción de pantalla ya provocan un redibujado normal.
        # No reiniciar la interacción aquí: puede vaciar el display por un
        # fotograma y producir una pantalla negra durante el movimiento.

    def click_casilla(x, y):
        # Ignorar clics del tablero mientras cualquier combate está activo.
        if getattr(store, "combate_versus_activo", False) or store.enemigos_moviendo:
            return
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
        enemigo_objetivo = None
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo() and enemigo.get_x() == x and enemigo.get_y() == y:
                enemigo_objetivo = enemigo
                break

        if enemigo_objetivo is not None:
            distancia = abs(enemigo_objetivo.get_x() - unidad.get_x()) + abs(enemigo_objetivo.get_y() - unidad.get_y())
            if distancia != 1:
                renpy.notify("Para combatir, debes tocar un enemigo adyacente.")
                return
            store.heroe_actual = unidad
            renpy.call_in_new_context("combate", unidad, enemigo_objetivo)
            store.unidad_seleccionada = None
            if store.combate_historia_huida:
                store.combate_historia_huida = False
                store.turno_jugador = True
                store.texto_turno = "Tu turno"
                return
        else:
            if (x, y) not in casillas_movimiento_historia(unidad):
                ocupada = False
                for otra in store.heroes + store.ejercito + store.enemigos:
                    if otra != unidad and otra.get_visible() and otra.esta_vivo() and otra.get_x() == x and otra.get_y() == y:
                        ocupada = True
                        break
                if ocupada:
                    renpy.notify("Esta casilla esta ocupada!")
                else:
                    renpy.notify("Solo puedes mover 1 casilla")
                return

            unidad.set_x(x)
            unidad.set_y(y)
            store.jugador_x = x
            store.jugador_y = y

        renpy.notify("Turno enemigo")
        store.turno_jugador = False
        store.texto_turno = "Turno enemigo"

        enemigos_vivos = [e for e in store.enemigos if e.get_visible() and e.esta_vivo()]
        # En cada respuesta enemiga se mueve una sola ficha. Elegir al azar
        # evita que el primer enemigo de la lista sea siempre el único activo.
        store.enemigos_pendientes = [random.choice(enemigos_vivos)] if enemigos_vivos else []
        store.enemigos_moviendo = bool(store.enemigos_pendientes)
        if not store.enemigos_moviendo:
            finalizar_turno_historia()
        # Al volver de la acción, Ren'Py redibuja el tablero automáticamente.

# ============================================================
# CLICK EN CASILLA (MODO VERSUS)
# ============================================================
init python:
    def click_casilla_versus(x, y):
        # Impide que clics durante el duelo muevan unidades o abran otro combate.
        if getattr(store, "combate_versus_activo", False):
            return
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
            if otra != unidad and otra.get_visible() and otra.esta_vivo() and otra.get_x() == x and otra.get_y() == y:
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
# COMBATE (MODO NORMAL)
# ============================================================
label combate(heroe, enemigo):
    $ combate_historia_huida = False
    $ combate_versus_atacante = heroe
    $ combate_versus_defensor = enemigo
    $ combate_versus_accion = "idle"
    $ combate_versus_resultado = ""
    $ combate_versus_activo = True
    show screen presentacion_combate_versus

    python:
        ia = None
        clase_enemigo = enemigo.get_clase()
        if "Sacerdotisa" in clase_enemigo: ia = IA_Sacerdotisa()
        elif "Demonia" in clase_enemigo: ia = IA_Demonia()
        elif "Licha" in clase_enemigo: ia = IA_Licha()
        elif "Archimago" in clase_enemigo: ia = IA_ArchiMago()
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
        $ clase = heroe.get_clase()
        $ accion_realizada = False
        $ vida_enemigo_inicial = enemigo.get_vida()

        # KAZUKI
        if clase == "Kazuki":
            $ info_k = "Kazuki - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_k]"
                "Atacar (Bola de Fuego) - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "BOLA DE FUEGO! [danio] de danio."
                "Bola de Fuego Mejorada - 20 magia":
                    $ danio = heroe.bola_fuego_mejorada(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Bola Mejorada! [danio] de danio."
                "Ataque Hielo Infernal - 10 magia":
                    $ danio = heroe.ataque_hielo_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Hielo Infernal! [danio] de danio."
                "Castigo Divino - 30 magia":
                    $ danio = heroe.ataque_castigo_divino(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Castigo Divino! [danio] de danio."
                "Vientos Infernales - 50 magia":
                    $ danio = heroe.vientos_infernales_prohibidos(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Vientos Infernales! [danio] de danio."
                "Waldgose - 100 magia":
                    $ danio = heroe.ataque_magico_prohibido(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "WALDGOSE! [danio] de danio."
                "Potenciar aliado (+20%%ATQ)":
                    $ heroe.potenciar_aliado(heroe)
                    $ accion_realizada = True
                    "Kazuki se potencia! ATQ: [heroe.get_ataque_basico()]"
                "Curacion Magica - 29 magia":
                    $ curado = heroe.curacion_magica()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Recuperar Magia +10":
                    $ heroe.recuperar_magia(reducir_estadistica(100))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # LYRA
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
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # GROMM
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
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # MAGO
        elif clase in ["Mago", "Mago2"]:
            $ info_m = "Mago - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_m]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Bola de Fuego Mejorada - 20 magia":
                    $ danio = heroe.bola_fuego_mejorada(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Bola! [danio] de danio."
                "Hielo Infernal - 10 magia":
                    $ danio = heroe.ataque_hielo_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Hielo! [danio] de danio."
                "Castigo Divino - 30 magia":
                    $ danio = heroe.ataque_castigo_divino(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia o usos!"
                    else:
                        $ accion_realizada = True
                        "Castigo! [danio] de danio."
                "Vientos Infernales - 50 magia":
                    $ danio = heroe.vientos_infernales_prohibidos(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Vientos! [danio] de danio."
                "Waldgose - 100 magia":
                    $ danio = heroe.ataque_magico_prohibido(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "WALDGOSE! [danio] de danio."
                "Curacion Magica - 29 magia":
                    $ curado = heroe.curacion_magica()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Recuperar Magia +10":
                    $ heroe.recuperar_magia(reducir_estadistica(100))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # ARCHIMAGO
        elif clase in ["Archimago", "Archimago2"]:
            $ info_a = "Archimago - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_a]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Ataque Especial - 30 magia":
                    $ danio = heroe.ataque_especial(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Especial! [danio] de danio."
                "Ataque Gelido - 26 magia":
                    $ danio = heroe.ataque_gelido(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Gelido! [danio] de danio."
                "Ataque Oscuro - 36 magia":
                    $ danio = heroe.ataque_oscuro(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Oscuro! [danio] de danio."
                "Espadas de Luz - 50 magia":
                    $ danio = heroe.ataque_espadas_magicas_de_luz(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espadas! [danio] de danio."
                "Relampago - 36 magia":
                    $ danio = heroe.ataque_magico_relampago(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Relampago! [danio] de danio."
                "Ataque Final - 100 magia":
                    $ danio = heroe.ataque_final(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "FINAL! [danio] de danio."
                "Curacion Magica - 29 magia":
                    $ curado = heroe.curacion_magica()
                    if curado == 0:
                        "No tienes suficiente magia o vida llena!"
                    else:
                        $ accion_realizada = True
                        "HP recuperado: [curado]"
                "Recuperar Magia +20":
                    $ heroe.recuperar_magia(reducir_estadistica(200))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # GUERRERO
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
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # ARQUERO
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
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # LICH
        elif clase in ["Lich", "Lich2"]:
            $ info_li = "Lich - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_li]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Ataque Espectral - 5 magia":
                    $ danio = heroe.ataque_espectral(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espectral! [danio] de danio."
                "Drenar Vida - 3 magia":
                    $ danio = heroe.drenar_vida(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Drenar! [danio] de danio. HP: [heroe.get_vida()]"
                "Ataque Masivo - 10 magia":
                    $ danio = heroe.ataque_masivo(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Masivo! [danio] de danio."
                "Curar - 4 magia":
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
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # CLERIGO
        elif clase in ["Clerigo", "Clerigo2"]:
            $ info_cl = "Clerigo - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_cl]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Palabras de Fe - 10 magia":
                    $ resultado = heroe.palabras_de_fe(enemigo)
                    if resultado == False:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "ATQ enemigo reducido a [enemigo.get_ataque_basico()]"
                "Luz Cegadora - 30 magia":
                    $ danio = heroe.luz_cegadora_dia(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Luz! [danio] de danio."
                "Exorcismo - 40 magia":
                    $ danio = heroe.exorcismo(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "EXORCISMO! [danio] de danio."
                "Escudo de Fe - 20 magia":
                    $ resultado = heroe.escudo_de_fe_magico()
                    if resultado == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "DEF: [heroe.get_defensa()]"
                "Recuperar Magia +20":
                    $ heroe.recuperacion_sagrada(reducir_estadistica(200))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # GENERAL
        elif clase in ["General", "General2"]:
            $ info_gen = "General - ENERGIA: " + str(heroe.get_energia())
            menu:
                "[info_gen]"
                "Espada - 10 energia":
                    $ danio = heroe.espada(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia! Recuperas 200."
                    else:
                        $ accion_realizada = True
                        "Corte! [danio] de danio. ENERGIA: [heroe.get_energia()]"
                "Canon de Mano - 25 energia":
                    $ danio = heroe.canon_de_mano(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia!"
                    else:
                        $ accion_realizada = True
                        "Canon! [danio] de danio. ENERGIA: [heroe.get_energia()]"
                "Tiro Doble - 35 energia":
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
                "Canon Final - 100 energia":
                    $ danio = heroe.canion_especial_final(enemigo)
                    if danio == 0:
                        "No tienes suficiente energia!"
                    else:
                        $ accion_realizada = True
                        "CANON FINAL! [danio] de danio."
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # DRAGON
        elif clase in ["Dragon", "Dragon2"]:
            $ info_dr = "Dragon - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_dr]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Golpe! [danio] de danio."
                "Llamarada Infernal - 20 magia":
                    $ danio = heroe.ataque_llamarada_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Llamarada! [danio] de danio."
                "Ataque de Espinas - 10 magia":
                    $ danio = heroe.ataque_espinas(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espinas! [danio] de danio."
                "Rayo de Luz - 15 magia":
                    $ danio = heroe.ataque_luz(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Rayo de Luz! [danio] de danio."
                "Escamas Reflectantes - 3 magia":
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
                "Recuperar Magia +10":
                    $ heroe.recuperacion_draconica(reducir_estadistica(100))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # SACERDOTISA
        elif clase == "Sacerdotisa":
            $ info_sac = "Sacerdotisa - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_sac]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Bendicion Divina - 35 magia (cura a todos)":
                    $ curados = heroe.bendicion_divina(store.heroes + store.ejercito)
                    if curados == 0:
                        "No tienes suficiente magia o nadie esta herido!"
                    else:
                        $ accion_realizada = True
                        "Curaste a [curados] aliados +120 HP."
                "Escudo Sagrado - 25 magia (+50 DEF)":
                    $ resultado = heroe.escudo_sagrado(heroe)
                    if resultado == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "DEF: [heroe.get_defensa()]"
                "Castigo Celestial - 50 magia":
                    $ danio = heroe.castigo_celestial(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "CASTIGO! [danio] de danio."
                "Palabras de Fe - 10 magia (-40%%ATQ enemigo)":
                    $ resultado = heroe.palabras_de_fe(enemigo)
                    if resultado == False:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "ATQ enemigo reducido a [enemigo.get_ataque_basico()]"
                "Luz Cegadora - 30 magia":
                    $ danio = heroe.luz_cegadora_dia(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Luz! [danio] de danio."
                "Exorcismo - 40 magia":
                    $ danio = heroe.exorcismo(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "EXORCISMO! [danio] de danio."
                "Recuperar Magia +20":
                    $ heroe.recuperacion_sagrada(reducir_estadistica(200))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # DEMONIA
        elif clase == "Demonia":
            $ info_dem = "Demonia - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max())
            menu:
                "[info_dem]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Golpe! [danio] de danio."
                "Latigazo Infernal - 20 magia (quema)":
                    $ danio = heroe.latigazo_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "LATIGAZO! [danio] de danio (con quemadura)."
                "Beso Drenante - 15 magia (roba vida)":
                    $ danio = heroe.beso_drenante(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "DRENAJE! [danio] de danio. HP: [heroe.get_vida()]"
                "Alas de Fuego - 30 magia (+30%%ATQ)":
                    $ resultado = heroe.alas_de_fuego()
                    if resultado == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "ATQ: [heroe.get_ataque_basico()] | MOV: [heroe.get_puntos_mov()]"
                "Explosion Infernal - 400 HP (daño masivo)":
                    $ danio = heroe.explosion_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente vida!"
                    else:
                        $ accion_realizada = True
                        "EXPLOSION! [danio] de danio. HP: [heroe.get_vida()]"
                "Llamarada Infernal - 20 magia":
                    $ danio = heroe.ataque_llamarada_infernal(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Llamarada! [danio] de danio."
                "Regeneracion":
                    $ restaurado = heroe.regeneracion_dragon()
                    $ accion_realizada = True
                    "HP recuperado: [restaurado]"
                "Recuperar Magia +10":
                    $ heroe.recuperacion_draconica(reducir_estadistica(100))
                    $ accion_realizada = True
                    "MAGIA: [heroe.get_magia()]"
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        # LICHA
        elif clase == "Licha":
            $ info_lic = "Licha - MAGIA: " + formato_recurso_combate(heroe.get_magia()) + "/" + formato_recurso_combate(heroe.get_magia_max()) + " | INVOC: " + str(heroe.get_invocaciones())
            menu:
                "[info_lic]"
                "Ataque basico - 10 magia":
                    $ danio = heroe.ataque_basico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia! Recuperas 50."
                    else:
                        $ accion_realizada = True
                        "Ataque! [danio] de danio."
                "Toque Helado - 10 magia (-20%%ATQ enemigo)":
                    $ danio = heroe.toque_helado(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "TOQUE HELADO! [danio] de danio. ATQ enemigo: [enemigo.get_ataque_basico()]"
                "Miasma Necrotico - 40 magia":
                    $ danio = heroe.miasma_necrotico(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "MIASMA! [danio] de danio."
                "Invocar Esqueleto - 25 magia":
                    $ resultado = heroe.invocar_esqueleto()
                    if resultado == False:
                        "No tienes suficiente magia o invocaciones!"
                    else:
                        $ accion_realizada = True
                        "Esqueleto invocado! Restantes: [heroe.get_invocaciones()]"
                "Drenaje Masivo - 20 magia":
                    $ danio = heroe.drenaje_masivo(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "DRENAJE! [danio] de danio. HP: [heroe.get_vida()] | MAGIA: [heroe.get_magia()]"
                "Maldicion - 30 magia (-50%%DEF enemigo)":
                    $ resultado = heroe.maldicion(enemigo)
                    if resultado == False:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "DEF enemigo reducida a [enemigo.get_defensa()]"
                "Ejercito de Muertos":
                    $ danio = heroe.ejercito_de_muertos(enemigo)
                    if danio == 0:
                        "No tienes invocaciones disponibles!"
                    else:
                        $ accion_realizada = True
                        "EJERCITO! [danio] de danio. Invocaciones: [heroe.get_invocaciones()]"
                "Ataque Espectral - 5 magia":
                    $ danio = heroe.ataque_espectral(enemigo)
                    if danio == 0:
                        "No tienes suficiente magia!"
                    else:
                        $ accion_realizada = True
                        "Espectral! [danio] de danio."
                "Curar - 4 magia":
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
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return


        else:
            menu:
                "[clase] - Que haras?"
                "Atacar":
                    $ danio = aplicar_danio_basico(heroe, enemigo)
                    $ accion_realizada = True
                    "Atacas. [danio] de danio."
                "Huir":
                    $ combate_historia_huida = True
                    "Escapaste!"
                    $ combate_versus_activo = False
                    $ restaurar_recursos_combate(heroe, enemigo)
                    hide screen presentacion_combate_versus
                    return

        if accion_realizada:
            $ combate_versus_resultado = "ataque" if enemigo.get_vida() < vida_enemigo_inicial else "accion"
            $ combate_versus_accion = "ataque"
            $ renpy.pause(0.45, hard=True)
            if combate_versus_resultado == "ataque":
                $ combate_versus_accion = "dano"
                $ renpy.pause(0.4, hard=True)
            $ combate_versus_accion = "idle"
            $ stats_post = get_stats_personaje(heroe)
            "[nombre_heroe] ahora tiene: [stats_post]"

        if not enemigo.esta_vivo():
            "[nombre_enemigo] HA SIDO DERROTADO!"
            $ registrar_muerte_enemigo()
            python:
                if es_boss(enemigo.get_clase()):
                    if nivel_actual >= 1 and nivel_actual <= 7:
                        registrar_boss_matado(nivel_actual)
            $ enemigo.set_visible(False)
            $ combate_versus_activo = False
            $ restaurar_recursos_combate(heroe, enemigo)
            hide screen presentacion_combate_versus
            return

        $ vida_heroe_inicial = heroe.get_vida()
        python:
            if ia is not None:
                try:
                    if "Clerigo" in enemigo.get_clase():
                        ia.evaluar(enemigo, heroe, store.enemigos)
                    else:
                        ia.evaluar(enemigo, heroe)
                except Exception as e:
                    print("[IA ERROR] " + str(e))
                    danio_enemigo = heroe.defenderse_recibir_danio(enemigo.get_ataque_basico())
                    renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")
            else:
                danio_enemigo = heroe.defenderse_recibir_danio(enemigo.get_ataque_basico())
                renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")

        if heroe.get_vida() < vida_heroe_inicial:
            $ combate_versus_accion = "defensor_ataca"
            $ renpy.pause(0.45, hard=True)
            $ combate_versus_accion = "defensor_dano"
            $ renpy.pause(0.4, hard=True)
            $ combate_versus_accion = "idle"

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
            $ combate_versus_activo = False
            $ restaurar_recursos_combate(heroe, enemigo)
            hide screen presentacion_combate_versus
            return
    $ combate_versus_activo = False
    $ restaurar_recursos_combate(heroe, enemigo)
    hide screen presentacion_combate_versus
    return

# ============================================================
# COMBATE VERSUS
# ============================================================
label combate_versus(atacante, defensor):
    $ combate_versus_atacante = atacante
    $ combate_versus_defensor = defensor
    $ combate_versus_accion = "idle"
    $ combate_versus_resultado = ""
    $ combate_versus_huida = False
    $ combate_versus_terminado = False
    $ combate_versus_activo = True
    show screen presentacion_combate_versus
    while atacante.esta_vivo() and defensor.esta_vivo() and not combate_versus_terminado:
        $ combate_versus_atacante = atacante
        $ combate_versus_defensor = defensor
        $ combate_versus_accion = "idle"
        call menu_habilidad_versus(atacante, defensor) from _call_menu_atk_vs

        if combate_versus_huida:
            "[atacante.get_clase()] se retira del combate."
            $ combate_versus_terminado = True
        else:
            if combate_versus_resultado == "ataque":
                $ combate_versus_accion = "ataque"
                $ renpy.pause(0.55, hard=True)
                $ combate_versus_accion = "dano"
                $ renpy.pause(0.45, hard=True)
                $ combate_versus_accion = "idle"
            elif combate_versus_resultado == "accion":
                $ combate_versus_accion = "ataque"
                $ renpy.pause(0.55, hard=True)
                $ combate_versus_accion = "idle"

            if not defensor.esta_vivo():
                $ defensor.set_visible(False)
                "[defensor.get_clase()] HA SIDO DERROTADO!"
                $ combate_versus_terminado = True
            else:
                $ combate_versus_atacante = defensor
                $ combate_versus_defensor = atacante
                $ combate_versus_accion = "idle"
                call menu_habilidad_versus(defensor, atacante) from _call_menu_def_vs

                if combate_versus_huida:
                    "[defensor.get_clase()] se retira del combate."
                    $ combate_versus_terminado = True
                else:
                    if combate_versus_resultado == "ataque":
                        $ combate_versus_accion = "defensor_ataca"
                        $ renpy.pause(0.55, hard=True)
                        $ combate_versus_accion = "defensor_dano"
                        $ renpy.pause(0.45, hard=True)
                        $ combate_versus_accion = "idle"
                    elif combate_versus_resultado == "accion":
                        $ combate_versus_accion = "defensor_ataca"
                        $ renpy.pause(0.55, hard=True)
                        $ combate_versus_accion = "idle"

                    if not atacante.esta_vivo():
                        $ atacante.set_visible(False)
                        "[atacante.get_clase()] HA SIDO DERROTADO!"
                        $ combate_versus_terminado = True

    $ restaurar_recursos_combate(atacante, defensor)
    $ combate_versus_activo = False
    hide screen presentacion_combate_versus
    $ combate_versus_huida = False
    $ combate_versus_terminado = False
    return


# ============================================================
# MENU DE HABILIDAD PARA VERSUS (CON HP VISIBLE)
# ============================================================
label menu_habilidad_versus(unidad, objetivo):
    $ clase_u = unidad.get_clase()
    $ clase_o = objetivo.get_clase()
    $ accion_realizada = False
    $ combate_versus_resultado = ""

    $ hp_u = "HP: " + formato_recurso_combate(unidad.get_vida()) + "/" + formato_recurso_combate(unidad.get_vida_max())
    $ hp_o = "HP: " + formato_recurso_combate(objetivo.get_vida()) + "/" + formato_recurso_combate(objetivo.get_vida_max())
    $ vida_objetivo_inicial = objetivo.get_vida()
    $ linea_objetivo = "Objetivo: " + clase_o + " - " + hp_o

    # ---------------- DEMONIA (hereda Dragon) ----------------
    if isinstance(unidad, store.Demonia):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Latigazo Infernal (20 magia)":
                $ danio = unidad.latigazo_infernal(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Latigazo! [danio] de danio."
            "Beso Drenante (15 magia)":
                $ danio = unidad.beso_drenante(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Drenaje! [danio] de danio."
            "Alas de Fuego (30 magia)":
                $ resultado = unidad.alas_de_fuego()
                if resultado == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "ATQ: [unidad.get_ataque_basico()]"
            "Recuperar Magia +10":
                $ unidad.recuperacion_draconica(reducir_estadistica(100))
                $ accion_realizada = True
                "MAGIA: [unidad.get_magia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- LICHA (hereda Lich) ----------------
    elif isinstance(unidad, store.Licha):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max()) + " | INVOC: " + str(unidad.get_invocaciones())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Toque Helado (10 magia)":
                $ danio = unidad.toque_helado(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Toque Helado! [danio] de danio."
            "Miasma Necrotico (40 magia)":
                $ danio = unidad.miasma_necrotico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Miasma! [danio] de danio."
            "Drenaje Masivo (20 magia)":
                $ danio = unidad.drenaje_masivo(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Drenaje! [danio] de danio."
            "Ejercito de Muertos":
                $ danio = unidad.ejercito_de_muertos(objetivo)
                if danio == 0:
                    "No tienes invocaciones disponibles!"
                else:
                    $ accion_realizada = True
                    "Ejercito! [danio] de danio."
            "Curar (4 magia)":
                $ curado = unidad.curar()
                if curado == 0:
                    "No tienes suficiente magia o vida llena!"
                else:
                    $ accion_realizada = True
                    "HP recuperado: [curado]"
            "Regenerar Magia":
                $ restaurado = unidad.regenerar_magia()
                $ accion_realizada = True
                "MAGIA restaurada: [restaurado]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- SACERDOTISA (hereda Clerigo) ----------------
    elif isinstance(unidad, store.Sacerdotisa):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Palabras de Fe (10 magia)":
                $ resultado = unidad.palabras_de_fe(objetivo)
                if resultado == False:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "ATQ enemigo reducido a [objetivo.get_ataque_basico()]"
            "Luz Cegadora (30 magia)":
                $ danio = unidad.luz_cegadora_dia(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Luz! [danio] de danio."
            "Castigo Celestial (50 magia)":
                $ danio = unidad.castigo_celestial(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Castigo! [danio] de danio."
            "Escudo Sagrado (25 magia)":
                $ resultado = unidad.escudo_sagrado(unidad)
                if resultado == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "DEF: [unidad.get_defensa()]"
            "Recuperar Magia +20":
                $ unidad.recuperacion_sagrada(reducir_estadistica(200))
                $ accion_realizada = True
                "MAGIA: [unidad.get_magia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- ARCHIMAGO ----------------
    elif isinstance(unidad, store.ArchiMago):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Ataque Especial (30 magia)":
                $ danio = unidad.ataque_especial(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Especial! [danio] de danio."
            "Ataque Gelido (26 magia)":
                $ danio = unidad.ataque_gelido(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Gelido! [danio] de danio."
            "Relampago (36 magia)":
                $ danio = unidad.ataque_magico_relampago(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Relampago! [danio] de danio."
            "Ataque Final (100 magia)":
                $ danio = unidad.ataque_final(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "FINAL! [danio] de danio."
            "Recuperar Magia +20":
                $ unidad.recuperar_magia(reducir_estadistica(200))
                $ accion_realizada = True
                "MAGIA: [unidad.get_magia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- LICH ----------------
    elif isinstance(unidad, store.Lich):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Ataque Espectral (5 magia)":
                $ danio = unidad.ataque_espectral(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Espectral! [danio] de danio."
            "Drenar Vida (3 magia)":
                $ danio = unidad.drenar_vida(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Drenar! [danio] de danio."
            "Ataque Masivo (10 magia)":
                $ danio = unidad.ataque_masivo(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Masivo! [danio] de danio."
            "Curar (4 magia)":
                $ curado = unidad.curar()
                if curado == 0:
                    "No tienes suficiente magia o vida llena!"
                else:
                    $ accion_realizada = True
                    "HP recuperado: [curado]"
            "Regenerar Magia":
                $ restaurado = unidad.regenerar_magia()
                $ accion_realizada = True
                "MAGIA restaurada: [restaurado]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- CLERIGO ----------------
    elif isinstance(unidad, store.Clerigo):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Palabras de Fe (10 magia)":
                $ resultado = unidad.palabras_de_fe(objetivo)
                if resultado == False:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "ATQ enemigo reducido a [objetivo.get_ataque_basico()]"
            "Luz Cegadora (30 magia)":
                $ danio = unidad.luz_cegadora_dia(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Luz! [danio] de danio."
            "Exorcismo (40 magia)":
                $ danio = unidad.exorcismo(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Exorcismo! [danio] de danio."
            "Escudo de Fe (20 magia)":
                $ resultado = unidad.escudo_de_fe_magico()
                if resultado == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "DEF: [unidad.get_defensa()]"
            "Recuperar Magia +20":
                $ unidad.recuperacion_sagrada(reducir_estadistica(200))
                $ accion_realizada = True
                "MAGIA: [unidad.get_magia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- DRAGON ----------------
    elif isinstance(unidad, store.Dragon):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Llamarada Infernal (20 magia)":
                $ danio = unidad.ataque_llamarada_infernal(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Llamarada! [danio] de danio."
            "Ataque de Espinas (10 magia)":
                $ danio = unidad.ataque_espinas(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Espinas! [danio] de danio."
            "Rayo de Luz (15 magia)":
                $ danio = unidad.ataque_luz(objetivo)
                if danio == 0:
                    "No tienes suficiente magia!"
                else:
                    $ accion_realizada = True
                    "Rayo de Luz! [danio] de danio."
            "Regeneracion":
                $ restaurado = unidad.regeneracion_dragon()
                $ accion_realizada = True
                "HP recuperado: [restaurado]"
            "Recuperar Magia +10":
                $ unidad.recuperacion_draconica(reducir_estadistica(100))
                $ accion_realizada = True
                "MAGIA: [unidad.get_magia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- MAGO ----------------
    elif isinstance(unidad, store.Mago):
        $ info_v = clase_u + " - " + hp_u + " | MAGIA: " + formato_recurso_combate(unidad.get_magia()) + "/" + formato_recurso_combate(unidad.get_magia_max())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Ataque basico (10 magia)":
                $ danio = unidad.ataque_basico(objetivo)
                if danio == 0:
                    "No tienes suficiente magia! Recuperas 50."
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Bola de Fuego Mejorada (20 magia)":
                $ danio = unidad.bola_fuego_mejorada(objetivo)
                if danio == 0:
                    "No tienes suficiente magia o usos!"
                else:
                    $ accion_realizada = True
                    "Bola! [danio] de danio."
            "Hielo Infernal (10 magia)":
                $ danio = unidad.ataque_hielo_infernal(objetivo)
                if danio == 0:
                    "No tienes suficiente magia o usos!"
                else:
                    $ accion_realizada = True
                    "Hielo! [danio] de danio."
            "Castigo Divino (30 magia)":
                $ danio = unidad.ataque_castigo_divino(objetivo)
                if danio == 0:
                    "No tienes suficiente magia o usos!"
                else:
                    $ accion_realizada = True
                    "Castigo! [danio] de danio."
            "Curacion Magica (29 magia)":
                $ curado = unidad.curacion_magica()
                if curado == 0:
                    "No tienes suficiente magia o vida llena!"
                else:
                    $ accion_realizada = True
                    "HP recuperado: [curado]"
            "Recuperar Magia +20":
                $ unidad.recuperar_magia(reducir_estadistica(200))
                $ accion_realizada = True
                "MAGIA: [unidad.get_magia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- GUERRERO ----------------
    elif isinstance(unidad, store.Guerrero):
        $ info_v = clase_u + " - " + hp_u + " | ATQ: " + str(unidad.get_ataque_basico()) + " | DEF: " + str(unidad.get_defensa())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Atacar":
                $ danio = unidad.ataque_basico(objetivo)
                $ accion_realizada = True
                "Hiciste [danio] de danio."
            "Testudo (+DEF x2)":
                $ unidad.testudo()
                $ accion_realizada = True
                "DEF: [unidad.get_defensa()]"
            "Arremeter (+20 ATQ)":
                $ unidad.arremeter()
                $ accion_realizada = True
                "ATQ: [unidad.get_ataque_basico()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- ARQUERO ----------------
    elif isinstance(unidad, store.Arquero):
        $ info_v = clase_u + " - " + hp_u + " | FLECHAS: " + str(unidad.get_carcaj()) + " | ESP: " + str(unidad.get_flecha_trucada())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Disparar Flecha":
                $ danio = unidad.disparar_flechas(objetivo)
                if danio == 0:
                    "No tienes flechas!"
                else:
                    $ accion_realizada = True
                    "Hiciste [danio] de danio."
            "Flecha Especial":
                $ danio = unidad.flechita_especial(objetivo)
                if danio == 0:
                    "No tienes flechas o esp!"
                else:
                    $ accion_realizada = True
                    "Especial! [danio] de danio."
            "Tiro Doble":
                $ danio = unidad.tiro_doble(objetivo)
                if danio == 0:
                    "No tienes flechas o esp!"
                else:
                    $ accion_realizada = True
                    "Tiro Doble! [danio] de danio."
            "Recargar Carcaj":
                $ unidad.recarga_rapida()
                $ accion_realizada = True
                "Flechas: [unidad.get_carcaj()] | Esp: [unidad.get_flecha_trucada()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- GENERAL ----------------
    elif isinstance(unidad, store.General):
        $ info_v = clase_u + " - " + hp_u + " | ENERGIA: " + str(unidad.get_energia())
        "[linea_objetivo]"
        menu:
            "[info_v]"
            "Espada (10 energia)":
                $ danio = unidad.espada(objetivo)
                if danio == 0:
                    "No tienes suficiente energia! Recuperas 200."
                else:
                    $ accion_realizada = True
                    "Corte! [danio] de danio. ENERGIA: [unidad.get_energia()]"
            "Canon de Mano (25 energia)":
                $ danio = unidad.canon_de_mano(objetivo)
                if danio == 0:
                    "No tienes suficiente energia!"
                else:
                    $ accion_realizada = True
                    "Canon! [danio] de danio. ENERGIA: [unidad.get_energia()]"
            "Tiro Doble (35 energia)":
                $ danio = unidad.tiro_doble(objetivo)
                if danio == 0:
                    "No tienes suficiente energia!"
                else:
                    $ accion_realizada = True
                    "Tiro Doble! [danio] de danio. ENERGIA: [unidad.get_energia()]"

            "Huir":
                $ combate_versus_huida = True
                return

    # ---------------- FALLBACK ----------------
    else:
        menu:
            "[clase_u] - [hp_u] - Que haras?"
            "Atacar":
                $ danio = aplicar_danio_basico(unidad, objetivo)
                $ accion_realizada = True
                "Hiciste [danio] de danio."

            "Huir":
                $ combate_versus_huida = True
                return

    if accion_realizada:
        $ combate_versus_resultado = "ataque" if objetivo.get_vida() < vida_objetivo_inicial else "accion"
    return

# ============================================================
# ARMAR EJERCITO
# ============================================================
label armar_ejercito:
    $ total = len(ejercito)

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (3, 4)]
        casillas_ocupadas = casillas_ocupadas_por_unidades(heroes + ejercito + enemigos)
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        px, py = random.choice(casillas_disponibles) if casillas_disponibles else (None, None)

    if total >= maxima_cantidad_unidades:
        "Ya tenes [maxima_cantidad_unidades] unidades. Ahora elegi un nivel:"
        jump elegir_nivel
    else:
        call screen seleccionar_unidad_ejercito(tipos_unidades_ejercito, total, maxima_cantidad_unidades, "ARMA TU EJÉRCITO")
        if _return == "__terminar__":
            if total == 0:
                "No tenes unidades, selecciona al menos una!"
                jump armar_ejercito
            else:
                jump elegir_nivel
        else:
            if px is None:
                "No hay casillas libres para agregar otra ficha."
            else:
                $ unidad = crear_unidad_ejercito(_return, px, py)
                $ ejercito.append(unidad)
            jump armar_ejercito

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
        "Nivel 7 - EL TRONO DE LA SEÑORA OSCURA":
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
        casillas_ocupadas = casillas_ocupadas_por_unidades(ejercito_j1 + ejercito_j2)
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        px, py = random.choice(casillas_disponibles) if casillas_disponibles else (None, None)

    if total >= maxima_cantidad_unidades:
        "Jugador 1 tiene [maxima_cantidad_unidades] unidades. Turno del Jugador 2."
        jump armar_ejercito_j2
    else:
        call screen seleccionar_unidad_ejercito(tipos_unidades_versus, total, maxima_cantidad_unidades, "JUGADOR 1 · ELIGE UNIDADES")
        if _return == "__terminar__":
            if total == 0:
                "Elegi al menos una unidad!"
                jump armar_ejercito_j1
            else:
                jump armar_ejercito_j2
        else:
            if px is None:
                "No hay casillas libres para el Jugador 1."
            else:
                $ ejercito_j1.append(crear_unidad_ejercito(_return, px, py, "J1"))
            jump armar_ejercito_j1

# ============================================================
# ARMAR EJERCITO J2 (VERSUS)
# ============================================================
label armar_ejercito_j2:
    $ total = len(ejercito_j2)

    python:
        posiciones_ejercito = [(x, y) for x in range(8) for y in (0, 1)]
        casillas_ocupadas = casillas_ocupadas_por_unidades(ejercito_j1 + ejercito_j2)
        casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
        px, py = random.choice(casillas_disponibles) if casillas_disponibles else (None, None)

    if total >= maxima_cantidad_unidades:
        "Jugador 2 tiene [maxima_cantidad_unidades] unidades. Empieza la batalla!"
        jump versus_inicio_batalla
    else:
        call screen seleccionar_unidad_ejercito(tipos_unidades_versus, total, maxima_cantidad_unidades, "JUGADOR 2 · ELIGE UNIDADES")
        if _return == "__terminar__":
            if total == 0:
                "Elegi al menos una unidad!"
                jump armar_ejercito_j2
            else:
                jump versus_inicio_batalla
        else:
            if px is None:
                "No hay casillas libres para el Jugador 2."
            else:
                $ ejercito_j2.append(crear_unidad_ejercito(_return, px, py, "J2"))
            jump armar_ejercito_j2

# ============================================================
# VERSUS
# ============================================================
label versus_inicio:
    $ modo_versus = True
    $ ejercito_j1 = []
    $ ejercito_j2 = []
    jump armar_ejercito_j1

label versus_inicio_batalla:
    $ turno_actual = 1
    $ texto_turno = "Turno Jugador 1"
    $ unidad_seleccionada = None
    $ partida_terminada = False
    $ resultado_batalla = ""
    $ tablero_actual = "nivel5.png"
    $ reparar_solapamientos_fichas(ejercito_j1 + ejercito_j2)
    $ reproducir_musica("versus.wav", fadein=1.0, loop=True)

    call screen tablero_versus

    if resultado_batalla == "j1_gana":
        jump versus_j1_gana
    elif resultado_batalla == "j2_gana":
        jump versus_j2_gana
    else:
        $ renpy.full_restart()

label versus_j1_gana:
    $ detener_musica(fadeout=1.0)
    "JUGADOR 1 GANA!"
    $ renpy.full_restart()

label versus_j2_gana:
    $ detener_musica(fadeout=1.0)
    "JUGADOR 2 GANA!"
    $ renpy.full_restart()

# ============================================================
# COMENZAR BATALLA
# ============================================================
label comenzar_batalla:
    "Tu ejercito esta listo!"
    "Mision: Elimina a todos los enemigos del tablero"
    $ partida_terminada = False
    $ resultado_batalla = ""
    $ boss_spawneado = False
    $ reparar_solapamientos_fichas(heroes + ejercito + enemigos)
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
    $ registrar_nivel_completado(nivel_actual) 

    if nivel_actual == 1:
        call dialogo_nivel1_victoria from _call_dialogo_nivel1_victoria
    elif nivel_actual == 2:
        call dialogo_nivel2_victoria from _call_dialogo_nivel2_victoria
    elif nivel_actual == 3:
        call dialogo_nivel3_victoria from _call_dialogo_nivel3_victoria
    elif nivel_actual == 4:
        call dialogo_nivel4_victoria from _call_dialogo_nivel4_victoria
    elif nivel_actual == 5:
        call dialogo_nivel5_victoria from _call_dialogo_nivel5_victoria
    elif nivel_actual == 6:
        call dialogo_nivel6_victoria from _call_dialogo_nivel6_victoria
    elif nivel_actual == 7:
        # Level 7 va directo al dialogo final, que a su vez lleva a la eleccion
        # (usa jump porque el dialogo NO retorna, encadena con el final)
        jump dialogo_nivel7_victoria
    else:
        "Nivel completado!"

    # Este bloque SOLO se ejecuta para niveles 1 a 6
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
        add tablero_actual:
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
                    hover_background "#FFFFFF20"
                    action Function(click_casilla, columna, fila)

        if unidad_seleccionada is not None and turno_jugador:
            for casilla in casillas_movimiento_historia(unidad_seleccionada):
                add Solid("#38D6EB55"):
                    xpos OFFSET_X + casilla[0] * CASILLA_W
                    ypos OFFSET_Y + casilla[1] * CASILLA_H
                    xsize CASILLA_W
                    ysize CASILLA_H

        for seleccionable in heroes + ejercito:
            if seleccionable.get_visible() and unidad_seleccionada == seleccionable:
                add Solid("#F3D38A66"):
                    xpos OFFSET_X + seleccionable.get_x() * CASILLA_W
                    ypos OFFSET_Y + seleccionable.get_y() * CASILLA_H
                    xsize CASILLA_W
                    ysize CASILLA_H

        for unidad in enemigos:
            if unidad.get_visible() and unidad.esta_vivo():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add im.Flip(obtener_imagen_enemigo(unidad.get_clase()), vertical=True)

        for heroe in heroes:
            if heroe.get_visible() and heroe.esta_vivo():
                frame:
                    xpos OFFSET_X + heroe.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + heroe.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add {"Kazuki": "Kazuki.png", "Lyra": "Lyra.png", "Gromm": "Gromm.png"}.get(heroe.get_clase(), "default.png")

        for unidad_ejercito in ejercito:
            if unidad_ejercito.get_visible() and unidad_ejercito.esta_vivo():
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

        timer 0.22 repeat True action If(enemigos_moviendo, Function(mover_siguiente_enemigo_turno), NullAction())
        timer 0.5 repeat True action If(partida_terminada, Return("fin"), NullAction())


# ============================================================
# SCREEN: TABLERO VERSUS (CON PANEL DE VIDA)
# ============================================================
screen tablero_versus():
    modal True
    fixed:
        add tablero_actual:
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

        # ---- EJERCITO J2 (arriba) ----
        for unidad in ejercito_j2:
            if unidad.get_visible() and unidad.esta_vivo():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add im.Flip(obtener_imagen_enemigo(unidad.get_clase()), vertical=True)

                frame:
                    background "#000000AA"
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 128
                    xsize 100
                    ysize 22
                    text (formato_recurso_combate(unidad.get_vida()) + "/" + formato_recurso_combate(unidad.get_vida_max())):
                        size 14
                        color "#FFFFFF"
                        xalign 0.5

        # ---- EJERCITO J1 (abajo) ----
        for unidad in ejercito_j1:
            if unidad.get_visible() and unidad.esta_vivo():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add obtener_imagen_enemigo(unidad.get_clase())

                frame:
                    background "#000000AA"
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 128
                    xsize 100
                    ysize 22
                    text (formato_recurso_combate(unidad.get_vida()) + "/" + formato_recurso_combate(unidad.get_vida_max())):
                        size 14
                        color "#FFFFFF"
                        xalign 0.5

        # Reborde de selección: se dibuja encima de las fichas para que destaque.
        if unidad_seleccionada is not None and unidad_seleccionada.get_visible() and unidad_seleccionada.esta_vivo():
            $ sx = OFFSET_X + unidad_seleccionada.get_x() * CASILLA_W + 21
            $ sy = OFFSET_Y + unidad_seleccionada.get_y() * CASILLA_H + 21
            add Solid("#FFE36E"):
                xpos sx
                ypos sy
                xsize 108
                ysize 4
            add Solid("#FFE36E"):
                xpos sx
                ypos sy + 104
                xsize 108
                ysize 4
            add Solid("#FFE36E"):
                xpos sx
                ypos sy
                xsize 4
                ysize 108
            add Solid("#FFE36E"):
                xpos sx + 104
                ypos sy
                xsize 4
                ysize 108

        # ---- PANEL IZQUIERDO: J1 ----
        frame:
            xpos 20
            ypos 20
            background "#00000088"
            padding (15, 10)
            vbox:
                spacing 5
                text "JUGADOR 1":
                    size 26
                    color "#88FF88"
                for u in ejercito_j1:
                    if u.get_visible() and u.esta_vivo():
                        text (u.get_clase() + ": " + str(u.get_vida()) + "/" + str(u.get_vida_max())):
                            size 18
                            color "#FFFFFF"

        # ---- PANEL DERECHO: J2 ----
        frame:
            xpos 1600
            ypos 20
            background "#00000088"
            padding (15, 10)
            vbox:
                spacing 5
                text "JUGADOR 2":
                    size 26
                    color "#FF8888"
                for u in ejercito_j2:
                    if u.get_visible() and u.esta_vivo():
                        text (u.get_clase() + ": " + str(u.get_vida()) + "/" + str(u.get_vida_max())):
                            size 18
                            color "#FFFFFF"

        # ---- TURNO ACTUAL ----
        frame:
            xpos 20
            ypos 1000
            background "#00000088"
            padding (15, 10)
            text texto_turno:
                size 30

        timer 0.5 repeat True action If(partida_terminada, Return("fin"), NullAction())


# Escena persistente del duelo: las barras reflejan la vida actual tras cada acción.
screen presentacion_combate_versus():
    zorder 5
    modal False
    add "#101522D9":
        xysize (1920, 1080)
    add "#24324BCC":
        xpos 120
        ypos 105
        xysize (1680, 720)

    text "DUELO":
        xpos 960
        ypos 130
        xanchor 0.5
        size 42
        bold True
        color "#F3D38A"

    $ izq_accion = "ataque" if combate_versus_accion == "ataque" else ("dano" if combate_versus_accion == "defensor_dano" else "idle")
    $ der_accion = "ataque" if combate_versus_accion == "defensor_ataca" else ("dano" if combate_versus_accion == "dano" else "idle")

    frame:
        xpos 205
        ypos 225
        xsize 580
        ysize 430
        background "#17202FEA"
        add obtener_sprite_combate(combate_versus_atacante.get_clase(), izq_accion):
            xalign 0.5
            yalign 0.48
            fit "contain"

    frame:
        xpos 1135
        ypos 225
        xsize 580
        ysize 430
        background "#17202FEA"
        add obtener_sprite_combate(combate_versus_defensor.get_clase(), der_accion):
            xalign 0.5
            yalign 0.48
            fit "contain"
            xzoom -1

    vbox:
        xpos 205
        ypos 660
        xsize 580
        spacing 10
        text combate_versus_atacante.get_clase():
            xalign 0.5
            size 30
            bold True
            color "#FFFFFF"
        bar:
            value StaticValue(fraccion_vida(combate_versus_atacante), 1.0)
            xsize 580
            ysize 30
            left_bar Solid("#55D68B")
            right_bar Solid("#452F3A")
        text "[formato_recurso_combate(combate_versus_atacante.get_vida())]/[formato_recurso_combate(combate_versus_atacante.get_vida_max())] HP":
            xalign 0.5
            size 22
            color "#DDE5F0"

    vbox:
        xpos 1135
        ypos 660
        xsize 580
        spacing 10
        text combate_versus_defensor.get_clase():
            xalign 0.5
            size 30
            bold True
            color "#FFFFFF"
        bar:
            value StaticValue(fraccion_vida(combate_versus_defensor), 1.0)
            xsize 580
            ysize 30
            left_bar Solid("#E45B63")
            right_bar Solid("#452F3A")
        text "[formato_recurso_combate(combate_versus_defensor.get_vida())]/[formato_recurso_combate(combate_versus_defensor.get_vida_max())] HP":
            xalign 0.5
            size 22
            color "#DDE5F0"

    if combate_versus_atacante.get_magia_max() > 0:
        hbox:
            xpos 205
            ypos 778
            xsize 580
            ysize 26
            spacing 8
            text "MAGIA":
                size 17
                color "#C8B7FF"
            bar:
                value StaticValue(fraccion_magia(combate_versus_atacante), 1.0)
                xsize 365
                ysize 18
                left_bar Solid("#8A72E8")
                right_bar Solid("#302A45")
            text "[formato_recurso_combate(combate_versus_atacante.get_magia())]/[formato_recurso_combate(combate_versus_atacante.get_magia_max())]":
                size 16
                color "#E5DEFF"

    if combate_versus_defensor.get_magia_max() > 0:
        hbox:
            xpos 1135
            ypos 778
            xsize 580
            ysize 26
            spacing 8
            text "MAGIA":
                size 17
                color "#C8B7FF"
            bar:
                value StaticValue(fraccion_magia(combate_versus_defensor), 1.0)
                xsize 365
                ysize 18
                left_bar Solid("#8A72E8")
                right_bar Solid("#302A45")
            text "[formato_recurso_combate(combate_versus_defensor.get_magia())]/[formato_recurso_combate(combate_versus_defensor.get_magia_max())]":
                size 16
                color "#E5DEFF"

    text "VS":
        xpos 960
        ypos 430
        xanchor 0.5
        size 48
        bold True
        color "#F3D38A"

    timer 0.1 repeat True action NullAction()


# ============================================================
# SCREEN: SELECCION DE HEROES
# ============================================================
screen seleccionar_unidad_ejercito(opciones, cantidad, maximo, encabezado):
    modal True
    zorder 50
    add "#101722E8":
        xysize (1920, 1080)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1530
        ysize 850
        padding (24, 20)
        background Frame(Solid("#24324BF5"), 18, 18)
        vbox:
            spacing 12
            text encabezado:
                xalign 0.5
                size 38
                bold True
                color "#F3D38A"
            text "Toca una tarjeta para agregar esa unidad · [cantidad]/[maximo]":
                xalign 0.5
                size 22
                color "#DDE5F0"

            grid 4 3:
                xalign 0.5
                spacing 12
                for i in range(12):
                    if i < len(opciones):
                        $ clase_unidad = opciones[i]
                        button:
                            xsize 350
                            ysize 225
                            padding (8, 8)
                            background Frame(Solid("#182536"), 10, 10)
                            hover_background Frame(Solid("#385879"), 10, 10)
                            action Return(clase_unidad)
                            vbox:
                                spacing 5
                                frame:
                                    xalign 0.5
                                    xsize 126
                                    ysize 160
                                    background "#0E1722"
                                    add obtener_imagen_retrato(clase_unidad):
                                        xalign 0.5
                                        yalign 0.5
                                        fit "contain"
                                text clase_unidad:
                                    xalign 0.5
                                    size 23
                                    bold True
                                    color "#FFFFFF"
                                text "TOCAR PARA AGREGAR":
                                    xalign 0.5
                                    size 13
                                    color "#D5A94F"
                    elif i == len(opciones):
                        button:
                            xsize 350
                            ysize 225
                            padding (8, 8)
                            background Frame(Solid("#2A3442"), 10, 10)
                            hover_background Frame(Solid("#4C5D70"), 10, 10)
                            action Return("__terminar__")
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 12
                                text "✓":
                                    xalign 0.5
                                    size 54
                                    color "#75D69A"
                                text "TERMINAR":
                                    xalign 0.5
                                    size 25
                                    bold True
                                    color "#FFFFFF"
                    else:
                        null width 350 height 225

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
    scene expression Solid("#ffffff")
    show expression "images/sanca_logo.jpg" as splash_logo:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.5, hard=True)
    return

# ============================================================
# LABEL START
# ============================================================
label minijuego_gkssj:
    $ iniciar_minijuego_gkssj()
    call screen minijuego_gkssj
    return

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
    call screen seleccion_heroes

    python:
        for h in heroes:
            if h != heroe_actual:
                h.set_visible(False)

    jump armar_ejercito

# ============================================================
# LABEL MENU PRINCIPAL
# ============================================================
label menu_principal:
    $ renpy.pause(1.5, hard=False)
    $ renpy.full_restart()
