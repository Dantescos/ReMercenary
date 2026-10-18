# ============================================================
# Sistema_musica.rpy
# ============================================================

init python:
    import os

    def resolver_archivo_audio(nombre):
        """Busca audio tanto en audio/ como en la raíz, tolerando extensión incorrecta."""
        nombre = nombre.replace("\\", "/").lstrip("/")
        rutas_base = [nombre]
        if nombre.startswith("audio/"):
            rutas_base.append(nombre[len("audio/"):])
        else:
            rutas_base.append("audio/" + nombre)

        extensiones = [os.path.splitext(nombre)[1]]
        extensiones.extend([".mp3", ".wav", ".ogg", ".opus"])
        extensiones = [ext for ext in extensiones if ext]

        revisadas = set()
        for ruta_base in rutas_base:
            sin_extension = os.path.splitext(ruta_base)[0]
            for extension in extensiones:
                ruta = sin_extension + extension
                if ruta not in revisadas:
                    revisadas.add(ruta)
                    if renpy.loadable(ruta):
                        return ruta

        raise IOError("No se encontro el archivo de audio: " + nombre)

    def reproducir_musica(nombre, fadein=1.0, loop=True):
        try:
            ruta = resolver_archivo_audio(nombre)
            renpy.music.play(ruta, fadein=fadein, loop=loop)
        except Exception as e:
            print("Error al reproducir " + nombre + ": " + str(e))

    def detener_musica(fadeout=1.0):
        renpy.music.stop(fadeout=fadeout)

    def reproducir_sonido(nombre, volume=1.0):
        try:
            ruta = resolver_archivo_audio(nombre)
            renpy.sound.play(ruta, volume=volume)
        except Exception as e:
            print("Error al reproducir sonido: " + str(e))

    def cambiar_musica(nombre, fadein=2.0, fadeout=1.0):
        renpy.music.stop(fadeout=fadeout)
        try:
            ruta = resolver_archivo_audio(nombre)
            renpy.music.play(ruta, fadein=fadein, loop=True)
        except Exception as e:
            print("Error al cambiar musica a " + nombre + ": " + str(e))

    def musica_volumen(volumen):
        renpy.music.set_volume(volumen, channel="music")
