screen menu_principal():
    frame:
        xfill True
        yfill True
        background "#0a0a1a"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            text "RE: MERCENARY" size 60 color "#ffcc00" bold True

            textbutton "Comenzar":
                action [Jump("level_one")]
                text_size 30

            textbutton "Salir":
                action Quit()