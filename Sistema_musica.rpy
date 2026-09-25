# ============================================================
# SISTEMA DE MUSICA - RE: MERCENARY
# ============================================================

init python:

    def reproducir_musica(nombre, fadein=1.0, loop=True):
        renpy.music.play("audio/" + nombre,    # Ruta completa
            fadein=fadein,        # Transicion de entrada
            loop=loop)       # Bucle o no

    def detener_musica(fadeout=1.0):
        renpy.music.stop(fadeout=fadeout)

    def reproducir_sonido(nombre, volume=1.0):
        renpy.sound.play("audio/" + nombre, volume=volume)

    def cambiar_musica(nombre, fadein=2.0, fadeout=1.0):

        renpy.music.play("audio/" + nombre,
            fadein=fadein,
            fadeout=fadeout,
            loop=True)

    def musica_volumen(volumen):
        renpy.music.set_volume(volumen, channel="music")

# ==========================================
# MUSICA PARA CONTEXTO
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

label level_one:
    $ reproducir_musica("Lvl1.wav")  
    "Comienza el Nivel 1..." # Poner un texto/pausa para escuchar la musica

label boss1:
    $ reproducir_musica("Boss1.wav") # Automaticamente reemplaza la musica anterior
    "¡Apareció el Jefe 1!"

label level_two:
    $ reproducir_musica("Lvl2.wav")
    "Entrando al Nivel 2..."

label boss2:
    $ reproducir_musica("Boss2.wav")
    "¡Jefe 2!"

label level_three:
    $ reproducir_musica("Lvl3.wav")
    "Nivel 3..."

label boss3:
    $ reproducir_musica("Boss3.wav")
    "¡Jefe 3!"

label level_four:
    $ reproducir_musica("Lv4.wav")
    "Nivel 4..."

label boss4:
    $ reproducir_musica("Boss4.wav")
    "¡Jefe 4!"

label level_five:
    $ reproducir_musica("Lvl5.wav")
    "Nivel 5..."

label boss5:
    $ reproducir_musica("Boss5.wav")
    "¡Jefe 5!"

label level_six:
    $ reproducir_musica("Lvl6.wav")
    "Nivel 6..."

label boss6:
    $ reproducir_musica("Boss6.wav")
    "¡Jefe 6!"

label level_seven:
    $ reproducir_musica("Lvl7.wav")
    "Nivel 7..."

label boss7:
    $ reproducir_musica("Boss7.wav")
    "¡Jefe Final!"