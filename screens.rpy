# ============================================================
# screens.rpy - Pantallas del juego
# ============================================================

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