# ============================================================
# RE: MERCENARY - CODIGO COMPLETO
# ============================================================
# VARIABLES GLOBALES
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
default ejercito = []          # Unidades que elige el jugador
default maxima_cantidad_unidades = 8  # Maximo 8 unidades
default enemigos = []
default enemigos_iniciales = []  # Guardamos los enemigos originales para resetear
default partida_terminada = False
# ============================================================
# INICIALIZACION Y CLASES
# ============================================================
init python:
    import random #aca estan las configuraciones del tablero
    COLUMNAS = 8
    FILAS = 5
    OFFSET_X = 180
    OFFSET_Y = 140
    CASILLA_W = 195
    CASILLA_H = 170
# ==========================================================
# MOVIMIENTO DE ENEMIGOS
# ==========================================================
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
# ==========================================================
# CREAR HEROES
# ==========================================================
    def crear_heroes():
        return [ Kazuki(2, 3), Lyra(4, 3), Gromm(6, 3) ]

# ==========================================================
# CREAR ENEMIGOS (FIJOS PARA EL TABLERO)
# ==========================================================
    def crear_enemigos():
        # Fila 0: 8 enemigos
        posiciones = [(x,y) for x in range(8) for y in [0,1]]
        random.shuffle(posiciones)

        enemigos = [] # aca se guardan en una lista como yo queria. Lo bueno que al ser una lista es como siempre con pop()  y demas metodos de lista
        x,y = posiciones.pop()
        enemigos.append(Mago("Mago", 200, 25, 15, 4, 3, 30, x, y, 0, True, 100, 10, 10, 10))
        x,y = posiciones.pop()
        enemigos.append(General("General", 250, 30, 20, 3, 2, 40, x,y, 0, True, 1000, 500))
        x,y = posiciones.pop()
        enemigos.append(Arquero("Arquero", 120, 25, 12, 4, 4, 30,x,y, 0, True, 30, 10))
        x,y = posiciones.pop()
        enemigos.append(Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, x,y, 0, True, 100))
        x,y = posiciones.pop()
        enemigos.append(Guerrero("Guerrero", 150, 40, 20, 4, 1, 35,x,y, 0, True))
        x,y = posiciones.pop()
        enemigos.append(Dragon("Dragon", 300, 60, 30, 2, 3, 70, x,y, 0, True, 500, 0, 0))
        x,y = posiciones.pop()
        enemigos.append(Lich("Lich", 180, 28, 20, 3, 2, 45,x,y, 0, True, 200))
        x,y = posiciones.pop()
        enemigos.append(ArchiMago("Archimago", 300, 35, 25, 3, 3, 50,x,y, 0, True, 1500, 100))
        # Fila 1: otros 8 enemigos (con nombres distintos para evitar conflictos)
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
# FUNCIONES DE INTERACCION
# ============================================================
init python:
    def click_casilla(x, y):
        if not store.turno_jugador:
            renpy.notify("Turno enemigo")
            return
        # Seleccionar heroe
        for heroe in store.heroes:
            if heroe.get_visible() and heroe.get_x() == x and heroe.get_y() == y:
                store.unidad_seleccionada = heroe
                store.heroe_actual = heroe
                renpy.notify("Seleccionado: " + heroe.get_clase())
                return
        # Seleccionar pieza del ejercito
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
        # PEQUEÑA PRUEBA QUE VOY A HACER QUE ME SUGERIO LA IA COSA QUE NO HICE ANTES PERO VEAMOS
        ocupada = False
        for otra in store.ejercito + store.heroes:
            if otra != unidad and otra.get_visible() and otra.get_x() == x and otra.get_y() == y:
                renpy.notify('Esta casilla esta ocupada!')
                renpy.notify('Elige otra ficha para mover!')
                return
        #Esto es para mover la unidad, setteo nuevas coordenas a la unidad 
        unidad.set_x(x)
        unidad.set_y(y)
        store.jugador_x = x #Para que el cursor azul siga a la unidad
        store.jugador_y = y

        renpy.notify("Turno enemigo")
        store.turno_jugador = False
        store.texto_turno = "Turno enemigo"
        mover_enemigos()

        store.turno_jugador = True
        store.texto_turno = "Tu turno"
        store.unidad_seleccionada = None
        renpy.notify("Tu turno")

    def actualizar_movimiento():#En teoria ya esta funcion NO la necesitamos, igual preguntar!
        if store.heroe_actual is None:
            return False

        movio = False
        heroe = store.heroe_actual

        if heroe.get_x() < store.destino_x:
            heroe.set_x(heroe.get_x() + 1)
            movio = True
        elif heroe.get_x() > store.destino_x:
            heroe.set_x(heroe.get_x() - 1)
            movio = True
        elif heroe.get_y() < store.destino_y:
            heroe.set_y(heroe.get_y() + 1)
            movio = True
        elif heroe.get_y() > store.destino_y:
            heroe.set_y(heroe.get_y() - 1)
            movio = True
            
        #aca se actualiza las coordenas para el cursor 
        store.jugador_x = heroe.get_x()
        store.jugador_y = heroe.get_y()

        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.get_x() == heroe.get_x() and enemigo.get_y() == heroe.get_y():
                renpy.call_in_new_context("combate", heroe, enemigo)
                break
        return movio

# ============================================================
# LABEL DE COMBATE
# ============================================================
label combate(heroe, enemigo):
    while heroe.esta_vivo() and enemigo.esta_vivo():
        # --- Turno del jugador ---
        if heroe.get_clase() == "Kazuki":
            $ heroe.potenciar_aliado(heroe)
            "Kazuki se potencia! ATQ +20%."
        elif heroe.get_clase() == "Lyra":
            $ danio = heroe.flecha_perforante(enemigo)  
            "Lyra usa sus flechas especiales!"
        elif heroe.get_clase() == "Gromm":
            $ heroe.escudo_levantado()
            "Gromm levanta su escudo! Defensa duplicada."  
        menu:
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
            "¡[  enemigo.get_clase()] ha muerto!"
            $ enemigo.set_visible(False)
        #Impongo condicion de victoria o por lo menos que mueran todos los enemigos
        if not quedan_enemigos_vivos():
            "¡Todos los enemigos han sido eliminados!"
            $ store.partida_terminada = True
            return
        # --- Turno del enemigo (IA) ---
        "El [enemigo.get_clase()] ataca!"
        $ danio_enemigo = enemigo.get_ataque_basico()
        $ heroe_defensa = heroe.defenderse_recibir_danio(danio_enemigo)
        " Te hizo [danio_enemigo] de daño"
        # Mostrar estado
        "[heroe.get_clase()] HP: [heroe.get_vida()] | [enemigo.get_clase()] HP: [enemigo.get_vida()]"
        if not heroe.esta_vivo():
            "¡[heroe.get_clase()] ha muerto!"
            $ heroe.set_visible(False)
            $ renpy.notify('GAME OVER!')
            jump derrotado
    return
# ============================================================
# FUNCION PARA VERIFICAR SI QUEDAN ENEMIGOS VIVOS
# ============================================================
init python:
    def quedan_enemigos_vivos():
        for enemigo in store.enemigos:
            if enemigo.get_visible() and enemigo.esta_vivo():
                return True
        return False
# ============================================================
# LABEL: ARMAR EJERCITO
# ============================================================
label armar_ejercito:
    $ total = len(ejercito)
    # Si ya tiene el maximo, salta a la batalla
    if total >= maxima_cantidad_unidades:
        "Ya tenes [maxima_cantidad_unidades] unidades. No podes agregar mas!"
        jump comenzar_batalla
    #aca voy a tener que usar lo siguiente para que aparezca al azar poque no funciona si no
python:
    posiciones_ejercito = [(x, y) for x in range(8) for y in (3, 4)]
    casillas_ocupadas = [(u.get_x(), u.get_y()) for u in ejercito]
    casillas_disponibles = [v for v in posiciones_ejercito if v not in casillas_ocupadas]
    if not casillas_disponibles:
        print("No hay casillas libres para desplegar!")
        #jump comenzar_batalla
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
                    "Nivel 1 - Goblins":
                        jump nivel1
                    "Nivel 2 - Fortaleza":
                        jump nivel2
                    "Nivel Aleatorio":
                        jump nivel_aleatorio
# ============================================================
# LABEL: COMENZAR BATALLA
# ============================================================
label comenzar_batalla:
    "¡Tu ejercito esta listo!"
    "Misión: ¡Elimina a todos los enemigos del tablero!"
    $ partida_terminada = False
    show screen tablero
    # En lugar de while True, usamos un loop con pausa y chequeos
    while True:
        $ renpy.pause(1.0)
        if not quedan_enemigos_vivos():
            jump victoria_jugador
        if heroe_actual is None or not heroe_actual.esta_vivo():
            jump derrotado
# ============================================================
# LABEL: VICTORIA Y DERROTA
# ============================================================
label victoria_jugador:
    hide screen tablero
    
    # Verificamos qué nivel se ganó y mostramos el diálogo correspondiente
    if nivel_actual == 1:
        call dialogo_nivel1_victoria
    elif nivel_actual == 2:
        "¡Nivel 2 completado!"
        "Kazuki,Gromm y Lyra han derrotado a la fortaleza enemiga."
    else:
        "¡Nivel completado!"
    
    menu:
        "¿Qué queres hacer?"
        "Jugar otro nivel":
            jump armar_ejercito
        "Reiniciar partida":
            jump reiniciar_partida
        "Salir al menú":
            jump menu_principal

label derrotado:
    hide screen tablero
    "GAME OVER. Tu heroe ha caido."
    menu:
        "¿Que queres hacer?"
        "Intentar de nuevo":
            jump reiniciar_partida
        "Salir al menu":
            jump menu_principal

label reiniciar_partida:
    # Reiniciamos todas las variables de cero
    $ ejercito = []
    $ enemigos = []
    $ heroe_actual = None
    $ unidad_seleccionada = None
    $ turno_jugador = True
    $ texto_turno = "Tu turno"
    $ partida_terminada = False
    $ jugador_x = 0
    $ jugador_y = 0
    $ destino_x = 0
    $ destino_y = 0
    # Volvemos al inicio para elegir heroe y armar ejercito
    jump inicio

label menu_principal:
    scene black
    call screen menu_principal

# ============================================================
# SCREEN: TABLERO
# ============================================================
screen tablero():
    modal True
    fixed:
        add "tablero.png":
            xsize 1920
            ysize 1080
        # Dibujar la cuadricula del tablero (8 filas x 10 columnas)
        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                button:
                    xpos OFFSET_X + columna * CASILLA_W
                    ypos OFFSET_Y + fila * CASILLA_H
                    xsize CASILLA_W
                    ysize CASILLA_H
                    background None
                    action Function(click_casilla, columna, fila)
# ======================================================
# ENEMIGOS (FILA 0 y 1)
# ======================================================
        for unidad in enemigos:
            if unidad.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad.get_y() * CASILLA_H + 25
                    xsize 100
                    ysize 100
                    add {"Dragon": "Dragon.png","Lich": "Lich.png","Archimago": "Archimago.png","Mago": "Mago.png",
                        "Clerigo": "Clerigo.png","Guerrero": "Guerrero.png","General": "General.png",
                        "Arquero": "Arquero.png"}.get(unidad.get_clase(),"default.png")
# ======================================================
# HEROE (FILA 4)
# ======================================================
        for heroe in heroes:
            if heroe.get_visible():
                if unidad_seleccionada == heroe:
                    add Solid("#FFFF0066"):
                        xpos OFFSET_X + heroe.get_x() * CASILLA_W
                        ypos OFFSET_Y + heroe.get_y() * CASILLA_H
                        xsize CASILLA_W
                        ysize CASILLA_H
                frame: #se usa un frame para envolver la imagen
                    xpos OFFSET_X + heroe.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + heroe.get_y() * CASILLA_H + 25
                    xsize 100  # Ajusta el ancho del sprite si se ve muy grande
                    ysize 100  # Ajusta el alto del sprite
                    add {"Kazuki":"Kazuki.png","Lyra": "Lyra.png", "Gromm": "Gromm.png"}.get(heroe.get_clase(), "default.png")
# ======================================================
# EJERCITO DEL JUGADOR 
# ======================================================
        for unidad_ejercito in ejercito:
            if unidad_ejercito.get_visible():
                frame:
                    background None
                    xpos OFFSET_X + unidad_ejercito.get_x() * CASILLA_W + 25
                    ypos OFFSET_Y + unidad_ejercito.get_y() * CASILLA_H + 25
                    xsize 56
                    ysize 56
                    add {"Dragon": "Dragon.png","Lich": "Lich.png","Archimago": "Archimago.png","Mago": "Mago.png","Clerigo": "Clerigo.png","Guerrero": "Guerrero.png","General": "General.png","Arquero": "Arquero.png"}.get(unidad_ejercito.get_clase(), "default.png")
# ======================================================
# CURSOR DEL JUGADOR
# ======================================================
        add Solid("#0000FF66"):
            xpos OFFSET_X + jugador_x * CASILLA_W
            ypos OFFSET_Y + jugador_y * CASILLA_H
            xsize CASILLA_W
            ysize CASILLA_H
# ======================================================
# TEXTO DEL TURNO
# ======================================================
        frame:
            xpos 20
            ypos 20
            background "#00000088"
            text texto_turno:
                size 30
    key "K_ESCAPE" action Return()
# ============================================================
# SCREEN: MENU PRINCIPAL
# ============================================================
screen menu_principal():
    frame:#agrego un frame para que el fondo se vea completo
        xfill True
        yfill True
        background "#0a0a1a"
        add "pantalla_inicio.png"
    vbox:
        xalign 0.5
        yalign 0.8
        textbutton "Comenzar" action Jump("inicio") xalign 0.5 text_size 30
        textbutton "Salir" action Quit() xalign 0.5 text_size 30
# ==============================================================
# PANTALLA DE SELECCION DE HEROE (SIN IMAGENES)
# ==============================================================
screen seleccion_heroes():
    modal True
    # Fondo de la pantalla 
    add "seleccion_heroe.png"
    # Marco semitransparente para que los botones se vean bien
    frame:
        background "#00000088"  # Fondo negro semitransparente
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            text "Elegi a tu heroe:" size 40 color "#ffffff" bold True
            
            # Botones de texto para cada heroe
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
# LABEL START (PUNTO DE ENTRADA DEL JUEGO)
# ============================================================
label start:
    $ reproducir_musica("main.wav", fadein=1.0, loop=True)
    call screen menu_principal #OJO si quieren ver lo del tablero y demas , TIENEN QUE BORRAR ESTO, LO HICE DE PRUEBA!

label inicio:
    scene black
    # Crear heroes y enemigos
    $ heroes   = crear_heroes()
    $ enemigos = crear_enemigos()
    "Bienvenido a RE: MERCENARY - Estrategia por turnos"
    call screen seleccion_heroes
    # Ocultar los heroes no elegidos
    python:
        for h in heroes:
            if h != heroe_actual:
                h.set_visible(False)
    "Has elegido a [heroe_actual.get_clase()]."
    "Ahora arma tu ejercito!"
    # Ir a armar el ejercito
    jump armar_ejercito
