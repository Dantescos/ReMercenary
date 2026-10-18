init python:
    config.game_menu_action = ShowMenu("pause_menu")


screen main_menu():
    tag menu

    on "show" action Play("music", "audio/inicio.wav", fadein=1.0, loop=True)

    frame:
        xfill True
        yfill True
        background "#0a0a1a"

    add "portada.png":
        xalign 0.5
        yalign 0.5

    vbox:
        xalign 0.5
        yalign 0.95
        spacing 15

        frame:
            background "#000000cc"
            padding (30, 15)

            vbox:
                spacing 10

                textbutton "Comenzar":
                    action Start()
                    xalign 0.5
                    text_size 30

                textbutton "Modo Versus (2 Jugadores)":
                    action Start("versus_inicio")
                    xalign 0.5
                    text_size 30

                textbutton "Cargar partida":
                    action ShowMenu("load")
                    xalign 0.5
                    text_size 30

                textbutton "Ver Logros":
                    action ShowMenu("pantalla_logros")
                    xalign 0.5
                    text_size 30

                textbutton "Lore":
                    action [Play("music", "audio/lore.wav", fadein=1.0, loop=True), ShowMenu("pantalla_lore")]
                    xalign 0.5
                    text_size 30

                textbutton "Créditos":
                    action [Play("music", "audio/creditos.wav", fadein=1.0, loop=True), ShowMenu("creditos_animados")]
                    xalign 0.5
                    text_size 30

                textbutton "Salir":
                    action Quit(confirm=False)
                    xalign 0.5
                    text_size 30

    frame:
        xalign 0.985
        yalign 0.985
        background "#080A12E8"
        padding (18, 14)
        vbox:
            spacing 8
            text "Código secreto":
                size 20
                color "#FFFFFF"
            input value VariableInputValue("codigo_secreto") length 5:
                xsize 280
                size 24
            if codigo_secreto.lower() == "gkssj":
                textbutton "Jugar Goku vs Freezer":
                    action Start("minijuego_gkssj")
                    text_size 20
            else:
                textbutton "Activar código":
                    action Function(renpy.notify, "Escribe el código gkssj.")
                    text_size 20


screen minijuego_gkssj():
    modal True
    add Solid("#111525")
    add Solid("#282A3A"):
        xpos 0
        ypos 860
        xsize 1920
        ysize 220
    add Solid("#E0A34A"):
        xpos 0
        ypos 856
        xsize 1920
        ysize 5

    text "GOKU SSJ  VS  FREEZER":
        xalign 0.5
        ypos 24
        size 38
        color "#FFE77A"
        outlines [(3, "#101020", 0, 0)]

    text "GOKU":
        xpos 52
        ypos 82
        size 23
        color "#FFFFFF"
    bar value goku_vida range 100:
        xpos 52
        ypos 116
        xsize 500
        ysize 28
        left_bar Solid("#45D66E")
        right_bar Solid("#4A2934")
    text "PODER":
        xpos 52
        ypos 153
        size 18
        color "#FFE77A"
    bar value goku_poder range 100:
        xpos 145
        ypos 158
        xsize 407
        ysize 18
        left_bar Solid("#63DDF4")
        right_bar Solid("#273143")

    text "FREEZER":
        xpos 1368
        ypos 82
        size 23
        color "#FFFFFF"
    bar value freezer_vida range 100:
        xpos 1368
        ypos 116
        xsize 500
        ysize 28
        left_bar Solid("#BD5BE8")
        right_bar Solid("#4A2934")

    add Transform(
        imagen_minijuego("goku", goku_accion, goku_frame),
        ysize=230,
        xanchor=0.5,
        yanchor=0.5,
        xzoom=(-1 if goku_accion in ("idle", "punch", "charge", "blast") and goku_facing < 0 else 1)
    ):
        xpos goku_x
        ypos goku_y

    add Transform(
        imagen_minijuego("freezer", freezer_accion, freezer_frame),
        ysize=230,
        xanchor=0.5,
        yanchor=0.5,
        xzoom=(-1 if freezer_accion in ("idle", "punch") and freezer_facing < 0 else 1)
    ):
        xpos freezer_x
        ypos freezer_y

    if mini_proyectil_activo:
        add Solid("#54E7FF"):
            xpos mini_proyectil_x - 30
            ypos mini_proyectil_y - 9
            xsize 60
            ysize 18
        add Solid("#FFFFFF"):
            xpos mini_proyectil_x - 18
            ypos mini_proyectil_y - 4
            xsize 36
            ysize 8

    frame:
        xpos 30
        ypos 970
        xsize 1860
        background "#080A12D8"
        padding (16, 12)
        text "W A S D: moverte    X: cargar poder (pulsa otra vez para parar)    C: disparar    Z: golpear":
            size 22
            color "#FFFFFF"

    text mini_resultado:
        xalign 0.5
        ypos 778
        size 28
        color "#FFE77A"
        outlines [(2, "#101020", 0, 0)]

    key ["w", "W"] action Function(minijuego_mover_goku, 0, -42, "up")
    key ["s", "S"] action Function(minijuego_mover_goku, 0, 42, "down")
    key ["a", "A"] action Function(minijuego_mover_goku, -42, 0, "left")
    key ["d", "D"] action Function(minijuego_mover_goku, 42, 0, "right")
    key ["x", "X"] action Function(minijuego_toggle_carga)
    key ["c", "C"] action Function(minijuego_disparar)
    key ["z", "Z"] action Function(minijuego_golpear)
    key "K_ESCAPE" action Return("salir")

    frame:
        xpos 1615
        ypos 865
        background "#080A12B8"
        padding (8, 6)
        vbox:
            spacing 3
            textbutton "↑":
                action Function(minijuego_mover_goku, 0, -42, "up")
                xalign 0.5
                text_size 25
            hbox:
                spacing 3
                textbutton "←":
                    action Function(minijuego_mover_goku, -42, 0, "left")
                    text_size 25
                textbutton "↓":
                    action Function(minijuego_mover_goku, 0, 42, "down")
                    text_size 25
                textbutton "→":
                    action Function(minijuego_mover_goku, 42, 0, "right")
                    text_size 25

    if not minijuego_activo:
        frame:
            xalign 0.5
            yalign 0.48
            background "#080A12E8"
            padding (35, 25)
            vbox:
                spacing 14
                text mini_resultado:
                    xalign 0.5
                    size 38
                    color "#FFE77A"
                textbutton "Jugar otra vez":
                    action Function(iniciar_minijuego_gkssj)
                    xalign 0.5
                    text_size 24
                textbutton "Volver al menú":
                    action Return("salir")
                    xalign 0.5
                    text_size 24

    timer 0.16 repeat True action Function(minijuego_tick)
    timer 0.35 repeat True action Function(minijuego_freezer_tick)


screen game_menu(title=None, scroll=None, yinitial=0.0):

    tag menu

    add "menu_pausa.png"

    if menu_pausa_activo:
        imagebutton:
            idle "coninuar_idle.png"
            hover "coninuar_hover.png"
            focus_mask True
            action Return()

    if menu_pausa_activo:
        imagebutton:
            idle "guardar_idle.png"
            hover "guardar_hover.png"
            focus_mask True
            action ShowMenu("save")

    if menu_pausa_activo:
        imagebutton:
            idle "cargar_idle.png"
            hover "cargar_hover.png"
            focus_mask True
            action ShowMenu("load")

    if menu_pausa_activo:
        imagebutton:
            idle "opciones_idle.png"
            hover "opciones_hover.png"
            focus_mask True
            action ShowMenu("preferences")

    if menu_pausa_activo:
        imagebutton:
            idle "kasuki_idle.png"
            hover "kasuki_hover.png"
            focus_mask True
            action ShowMenu("pantalla_logros")

    if menu_pausa_activo:
        imagebutton:
            idle "menu_idle.png"
            hover "menu_hover.png"
            focus_mask True
            action MainMenu()

    if menu_pausa_activo:
        imagebutton:
            idle "salir_idle.png"
            hover "salir_hover.png"
            focus_mask True
            action Quit(confirm=True)


screen save():

    tag menu

    add "negro2.png"

    use file_slots("Guardar")
    imagebutton:
        idle "volver_idle.png"
        hover "volver_hover.png"
        focus_mask True

        action Return()


screen load():

    tag menu

    add "negro1.png"

    use file_slots("Cargar")

    imagebutton:
        idle "volver_idle.png"
        hover "volver_hover.png"
        focus_mask True

        action Return()


screen file_slots(title):

    tag menu

    text title:
        xalign 0.5
        ypos 20
        size 50
        color "#FFFFFF"

    grid 3 2:

        xalign 0.5
        yalign 0.45

        spacing 20

        for i in range(6):

            $ slot = i + 1

            button:

                xsize 350
                ysize 220

                action FileAction(slot)

                has vbox

                add FileScreenshot(slot):
                    xalign 0.5

                text FileTime(
                    slot,
                    format="%d/%m/%Y %H:%M",
                    empty="Ranura vacía"
                ):
                    xalign 0.5

                text FileSaveName(slot):
                    xalign 0.5

                key "save_delete" action FileDelete(slot)

    hbox:

        xalign 0.5
        ypos 700

        spacing 10

        textbutton "<":
            action FilePagePrevious()

        for page in range(1, 11):

            textbutton "[page]":
                action FilePage(page)

        textbutton ">":
            action FilePageNext()

    textbutton "Volver":

        xalign 0.5
        ypos 760

        action Return()


screen choice(items):
    style_prefix "choice"
    zorder 20

    if combate_versus_activo:
        frame:
            xalign 0.5
            yalign 1.0
            xsize 1640
            ysize 270
            padding (14, 10)
            background "#101722F2"
            hbox:
                spacing 16
                for columna in range(2):
                    vbox:
                        spacing 5
                        for i in range(len(items)):
                            if i % 2 == columna:
                                button:
                                    xsize 790
                                    ysize 44
                                    padding (10, 3)
                                    background Frame(Solid("#202E40"), 8, 8)
                                    hover_background Frame(Solid("#385879"), 8, 8)
                                    action items[i].action
                                    hbox:
                                        spacing 12
                                        yalign 0.5
                                        frame:
                                            xsize 34
                                            ysize 34
                                            background Frame(Solid("#D5A94F"), 8, 8)
                                            text icono_accion_menu(items[i].caption):
                                                xalign 0.5
                                                yalign 0.5
                                                size 23
                                                bold True
                                                color "#182536"
                                        text items[i].caption:
                                            yalign 0.5
                                            size 20
                                            color "#F3F6FB"
    else:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            for i in items:
                textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 10

style choice_button:
    xalign 0.5
    xminimum 720
    padding (32, 16)
    background Frame(Solid("#182536EE"), 12, 12)
    hover_background Frame(Solid("#315579F5"), 12, 12)
    insensitive_background Frame(Solid("#18253688"), 12, 12)

style choice_button_text:
    xalign 0.5
    size 26
    color "#F3F6FB"
    hover_color "#FFE19A"
    outlines [(2, "#101722", 0, 0)]

default menu_pausa_activo = True

screen pause_menu():

    tag menu

    add "menu_pausa.png"

    if menu_pausa_activo:
        imagebutton:
            idle "coninuar_idle.png"
            hover "coninuar_hover.png"
            focus_mask True
            action Return()

    if menu_pausa_activo:
        imagebutton:
            idle "guardar_idle.png"
            hover "guardar_hover.png"
            focus_mask True
            action ShowMenu("save")

    if menu_pausa_activo:
        imagebutton:
            idle "cargar_idle.png"
            hover "cargar_hover.png"
            focus_mask True
            action ShowMenu("load")

    if menu_pausa_activo:
        imagebutton:
            idle "opciones_idle.png"
            hover "opciones_hover.png"
            focus_mask True
            action ShowMenu("preferences")

    if menu_pausa_activo:
        imagebutton:
            idle "kasuki_idle.png"
            hover "kasuki_hover.png"
            focus_mask True
            action ShowMenu("pantalla_logros")

    if menu_pausa_activo:
        imagebutton:
            idle "menu_idle.png"
            hover "menu_hover.png"
            focus_mask True
            action MainMenu()

    if menu_pausa_activo:
        imagebutton:
            idle "salir_idle.png"
            hover "salir_hover.png"
            focus_mask True
            action Quit(confirm=True)


# ============================================================
# SCREEN: CREDITOS ANIMADOS
# ============================================================
screen creditos_animados():
    tag menu
    modal True

    on "show" action Play("music", "audio/creditos.wav", fadein=1.0, loop=True)

    frame:
        xfill True
        yfill True
        background "#000000"

    vbox:
        xalign 0.5
        spacing 20
        at creditos_scroll

        text "RE: MERCENARY":
            xalign 0.5
            size 70
            color "#ffcc00"
            bold True

        null height 100

        text "EQUIPO DE DESARROLLO":
            xalign 0.5
            size 35
            color "#ffffff"

        null height 30
        text "Antonio Garcia":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Nahuel Villafañe":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Mateo Dabruzzo Wilczek":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Federico 'Fedelobo'":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Ignacio":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Thiago":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Pablo Laporta":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Fernando 'Master'":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Joaquin Arana":
            xalign 0.5
            size 28
            color "#cccccc"

        null height 60

        text "PROGRAMACION":
            xalign 0.5
            size 35
            color "#ffffff"
        null height 30
        text "Antonio Garcia":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Nahuel Villafañe":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Mateo Dabruzzo Wilczek":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Federico 'Fedelobo'":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Ignacio":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Thiago":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Pablo Laporta":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Fernando 'Master'":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Joaquin Arana":
            xalign 0.5
            size 28
            color "#cccccc"

        null height 60

        text "ARTE Y DISEÑO":
            xalign 0.5
            size 35
            color "#ffffff"
        null height 30
        text "Antonio Garcia":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Nahuel Villafañe":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Mateo Dabruzzo Wilczek":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Federico 'Fedelobo'":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Ignacio":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Thiago":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Pablo Laporta":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Fernando 'Master'":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Joaquin Arana":
            xalign 0.5
            size 28
            color "#cccccc"

        null height 60

        text "AGRADECIMIENTOS":
            xalign 0.5
            size 35
            color "#ffffff"

        null height 30

        text "A nuestras familias, Marcos (nuestro auxiliar) y amigos":
            xalign 0.5
            size 28
            color "#cccccc"

        null height 200

        text "© 2026 Equipo RE: MERCENARY":
            xalign 0.5
            size 20
            color "#888888"

        null height 500

    textbutton "Volver al menu":
        xalign 0.98
        yalign 0.98
        text_size 24
        text_color "#888888"
        text_hover_color "#ffffff"
        action Return()

    timer 28.0 action Return()


transform creditos_scroll:
    ypos 1.0
    linear 25.0 ypos -1.5

## ============================================================
# TAMAÑOS DE TEXTO GRANDES Y CENTRADOS
# ============================================================

# Dialogos de los personajes (abajo del juego)
style say_dialogue:
    size 38
    line_spacing 8
    xalign 0.5
    text_align 0.5

# El nombre del personaje que habla
style say_label:
    size 42
    bold True
    xalign 0.5
    text_align 0.5

# Titulo del menu (ej: "Kazuki - MAGIA: 100/250")
style menu_label:
    size 34
    color "#ffff88"
    bold True
    xalign 0.5
    text_align 0.5

# Menus de opciones (Atacar, Huir, etc)
style choice_button_text:
    size 30
    xalign 0.5
    text_align 0.5

# Texto narrativo
style say_thought:
    size 38
    xalign 0.5
    text_align 0.5

# Texto de los notifies (mensajes)
style notify_text:
    size 26
    xalign 0.5
    text_align 0.5

# Texto de los botones generales
style button_text:
    size 30
    xalign 0.5
    text_align 0.5

# Texto de los labels de input
style input_prompt:
    size 32
    xalign 0.5
    text_align 0.5

style window:
    ysize 280
    background "#000000cc"
    padding (60, 30)
    xalign 0.5

style namebox:
    xsize 400
    padding (30, 10)
    xalign 0.5
