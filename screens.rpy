init python:
    config.game_menu_action = ShowMenu("pause_menu")
    


screen main_menu():
    tag menu

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
