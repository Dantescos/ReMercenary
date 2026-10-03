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
# MOVIMIENTO DE ENEMIGOS
# ============================================================
init python:
    def mover_enemigos():
        heroe = store.heroe_actual
        if heroe is None:
            return
        for enemigo in store.enemigos[:]:
            if not enemigo.get_visible():
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
# INTERACCIÓN: CLICK EN CASILLA (MODO NORMAL)
# ============================================================
init python:
    def click_casilla(x, y):
        if not store.turno_jugador:
            renpy.notify("Turno enemigo")
            return

        for heroe in store.heroes:
            if heroe.get_visible() and heroe.get_x() == x and heroe.get_y() == y:
                store.unidad_seleccionada = heroe
                store.heroe_actual = heroe
                renpy.notify("Seleccionado: " + heroe.get_clase())
                return

        for unidad in store.ejercito:
            if unidad.get_visible() and unidad.get_x() == x and unidad.get_y() == y:
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
                reproducir_musica("Boss" + str(store.nivel_actual) + ".wav", fadein=0.5, loop=True)
                renpy.notify("¡BOSS! ¡Queda 1 enemigo!")

        store.turno_jugador = True

        store.turno_jugador = True
        store.texto_turno = "Tu turno"
        store.unidad_seleccionada = None
        renpy.notify("Tu turno")

        # Chequear fin de batalla
        if not quedan_enemigos_vivos():
            store.resultado_batalla = "victoria"
            store.partida_terminada = True
            return

        if store.heroe_actual is None or not store.heroe_actual.esta_vivo():
            store.resultado_batalla = "derrota"
            store.partida_terminada = True
            return

# ============================================================
# INTERACCIÓN: CLICK EN CASILLA (MODO VERSUS)
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
            if unidad.get_visible() and unidad.get_x() == x and unidad.get_y() == y:
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
            if enemigo.get_visible() and enemigo.get_x() == x and enemigo.get_y() == y:
                renpy.call_in_new_context("combate_versus", unidad, enemigo)
                cambiar_turno()
                # Chequear victoria
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
# FUNCIONES AUXILIARES
# ============================================================
init python:
    def cambiar_turno():
        if store.turno_actual == 1:
            store.turno_actual = 2
            store.texto_turno = "Turno Jugador 2"
        else:
            store.turno_actual = 1
            store.texto_turno = "Turno Jugador 1"
        store.unidad_seleccionada = None

    def hay_unidades_vivas(ejercito):
        for unidad in ejercito:
            if unidad.get_visible() and unidad.esta_vivo():
                return True
        return False

    def quedan_enemigos_vivos():
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo():
                return True
        return False

    def guardar_partida(slot="partida"):
        renpy.save(slot)
        store.partida_guardada = True
        store.slot_guardado = slot
        renpy.notify("Partida guardada.")

# ============================================================
# LABEL DE COMBATE (MODO NORMAL)
# ============================================================
label combate(heroe, enemigo):
    python:
        ia = None
        if "ArchiMago" in enemigo.get_clase():
            ia = IA_ArchiMago()
        elif "Lich" in enemigo.get_clase():
            ia = IA_Lich()
        elif "Clerigo" in enemigo.get_clase():
            ia = IA_Clerigo()
        elif "Guerrero" in enemigo.get_clase():
            ia = IA_Guerrero()
        elif "Arquero" in enemigo.get_clase():
            ia = IA_Arquero()
        elif "Dragon" in enemigo.get_clase():
            ia = IA_Dragon()
        elif "Mago" in enemigo.get_clase():
            ia = IA_Mago()
        elif "General" in enemigo.get_clase():
            ia = IA_General()
        else:
            ia = None

    while heroe.esta_vivo() and enemigo.esta_vivo():
        if heroe.get_clase() == "Kazuki":
            $ heroe.potenciar_aliado(heroe)
            "Kazuki se potencia! ATQ +20%%."
        elif heroe.get_clase() == "Lyra":
            $ danio = heroe.flecha_perforante(enemigo)
            "Lyra usa sus flechas especiales!"
        elif heroe.get_clase() == "Gromm":
            $ heroe.escudo_levantado()
            "Gromm levanta su escudo! Defensa duplicada."

        menu:
            "¿Que haras?"
            "Atacar":
                $ danio = heroe.get_ataque_basico()
                $ enemigo.defenderse_recibir_danio(danio)
                "Le hiciste [danio] de danio a [enemigo.get_clase()]."
            "Defender":
                $ heroe.set_defensa(heroe.get_defensa() + 10)
                "Te defendiste! +10 de defensa temporal."
            "Huir":
                "Escapaste!"
                return

        if not enemigo.esta_vivo():
            "¡[enemigo.get_clase()] ha muerto!"
            $ enemigo.set_visible(False)
            $ registrar_muerte_enemigo()
            return

        python:
            if ia is not None:
                if "Clerigo" in enemigo.get_clase():
                    ia.evaluar(enemigo, heroe, store.enemigos)
                else:
                    ia.evaluar(enemigo, heroe)
            else:
                danio_enemigo = enemigo.get_ataque_basico()
                heroe.defenderse_recibir_danio(danio_enemigo)
                renpy.say("", "Te hizo " + str(danio_enemigo) + " de danio.")

        "[heroe.get_clase()] HP: [heroe.get_vida()] | [enemigo.get_clase()] HP: [enemigo.get_vida()]"

        if not heroe.esta_vivo():
            "¡[heroe.get_clase()] ha muerto!"
            $ heroe.set_visible(False)
            jump derrotado
    return

# ============================================================
# LABEL DE COMBATE (MODO VERSUS)
# ============================================================
label combate_versus(atacante, defensor):
    while atacante.esta_vivo() and defensor.esta_vivo():
        $ danio = atacante.get_ataque_basico()
        $ defensor.defenderse_recibir_danio(danio)
        "[atacante.get_clase()] ataca a [defensor.get_clase()] por [danio] de danio!"

        if not defensor.esta_vivo():
            "[defensor.get_clase()] ha caido!"
            $ defensor.set_visible(False)
            return

        $ contra = defensor.get_ataque_basico() // 2
        $ atacante.defenderse_recibir_danio(contra)
        "[defensor.get_clase()] contraataca por [contra] de danio!"

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
        "Elegi una unidad para tu ejercito:"
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
# ARMAR EJERCITO JUGADOR 1 (VERSUS)
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
        "JUGADOR 1 - Elegi una unidad:"
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
# ARMAR EJERCITO JUGADOR 2 (VERSUS)
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
        "JUGADOR 2 - Elegi una unidad:"
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
# COMENZAR BATALLA (NORMAL)
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
# VICTORIA Y DERROTA
# ============================================================
label victoria_jugador:
    hide screen tablero
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
    else:
        "¡Nivel completado!"

    menu:
        "¿Que queres hacer?"
        "Jugar otro nivel":
            jump armar_ejercito
        "Reiniciar partida":
            jump reiniciar_partida
        "Salir al menu":
            $ renpy.full_restart()

label derrotado:
    hide screen tablero
    "GAME OVER. Tu heroe ha caido."
    menu:
        "¿Que queres hacer?"
        "Intentar de nuevo":
            jump reiniciar_partida
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
    $ jugador_x = 0
    $ jugador_y = 0
    $ destino_x = 0
    $ destino_y = 0
    $ modo_versus = False
    $ ejercito_j1 = []
    $ ejercito_j2 = []
    jump inicio

# ============================================================
# SCREEN: TABLERO (MODO NORMAL)
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

        # Timer que detecta fin de batalla y cierra la screen
        timer 0.5 repeat True action If(partida_terminada, Return(), NullAction())

    key "K_ESCAPE" action Return()

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

        # Timer que detecta fin de batalla y cierra la screen
        timer 0.5 repeat True action If(partida_terminada, Return(), NullAction())

    key "K_ESCAPE" action Return()

# ============================================================
# SCREEN: SELECCION DE HEROES
# ============================================================
screen seleccion_heroes():
    modal True

    add "seleccion_heroe.png"

    frame:
        background "#00000088"
        xfill True
        yfill True

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            text "Elegi a tu heroe:" size 40 color "#ffffff" bold True

            textbutton "Kazuki (Estratega)":
                action [SetVariable("heroe_actual", heroes[0]), Return()]
                text_size 30
                xalign 0.5

            textbutton "Lyra (Arquera Elfa)":
                action [SetVariable("heroe_actual", heroes[1]), Return()]
                text_size 30
                xalign 0.5

            textbutton "Gromm (Caballero Enano)":
                action [SetVariable("heroe_actual", heroes[2]), Return()]
                text_size 30
                xalign 0.5

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
    $ reproducir_musica("main.wav", fadein=1.0, loop=True)
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