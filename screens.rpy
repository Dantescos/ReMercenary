screen main_menu():
    frame:
        xfill True
        yfill True
        background "#0a0a1a"
        
        # Usar el nombre EXACTO del archivo
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
                    action Jump("inicio")
                    xalign 0.5
                    text_size 30
                
                textbutton "Salir":
                    action Quit()
                    xalign 0.5
                    text_size 30