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


screen game_menu(title=None, scroll=None, yinitial=0.0):

    tag menu

    add "menu_pausa.png"

    if menu_pausa_activo:
        imagebutton:
            idle "continuar_idle.png"
            hover "continuar_hover.png"
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
    padding (40, 12)
    background "#1a1a2ecc"
    hover_background "#4a4a8acc"

style choice_button_text:
    xalign 0.5
    size 28
    color "#ffffff"
    hover_color "#ffff88"

default menu_pausa_activo = True

screen pause_menu():

    tag menu

    add "menu_pausa.png"

    if menu_pausa_activo:
        imagebutton:
            idle "continuar_idle.png"
            hover "continuar_hover.png"
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

        text "Nahuel Zanini":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Mateo Dabruzzo Wilczek":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Federico 'Fedelobo' ":
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
        
        text "Fernando 'Master":
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

        text "Nahuel Zanini":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Mateo Dabruzzo Wilczek":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Federico 'Fedelobo' ":
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
        
        text "Fernando 'Master":
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

        text "Nahuel Zanini":
            xalign 0.5
            size 28
            color "#cccccc"

        text "Mateo Dabruzzo Wilczek":
            xalign 0.5
            size 28
            color "#cccccc"
        
        text "Federico 'Fedelobo' ":
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
        
        text "Fernando 'Master":
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

        text "A nuestras familias y amigos":
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
