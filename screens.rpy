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

                textbutton "Salir":
                    action Quit(confirm=False)
                    xalign 0.5
                    text_size 30