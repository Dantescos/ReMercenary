# ============================================================
# Sistema_musica.rpy
# ============================================================

init python:
    def reproducir_musica(nombre, fadein=1.0, loop=True):
        try:
            renpy.music.play("audio/" + nombre, fadein=fadein, loop=loop)
        except Exception as e:
            print("Error al reproducir " + nombre + ": " + str(e))

    def detener_musica(fadeout=1.0):
        renpy.music.stop(fadeout=fadeout)

    def reproducir_sonido(nombre, volume=1.0):
        try:
            renpy.sound.play("audio/" + nombre, volume=volume)
        except Exception as e:
            print("Error al reproducir sonido: " + str(e))

    def cambiar_musica(nombre, fadein=2.0, fadeout=1.0):
        renpy.music.stop(fadeout=fadeout)
        renpy.music.play("audio/" + nombre, fadein=fadein, loop=True)

    def musica_volumen(volumen):
        renpy.music.set_volume(volumen, channel="music")