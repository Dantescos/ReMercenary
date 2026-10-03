# ============================================================
# logros.rpy - Sistema de logros y rangos
# ============================================================

default enemigos_muertos_total = 0
default rango_actual = "Novato"

init python:
    def registrar_muerte_enemigo():
        store.enemigos_muertos_total += 1
        verificar_rango()

    def verificar_rango():
        total = store.enemigos_muertos_total
        rango_anterior = store.rango_actual
        if total >= 2000:
            nuevo_rango = "Leyenda"
        elif total >= 1000:
            nuevo_rango = "Experto"
        elif total >= 600:
            nuevo_rango = "Maestro"
        elif total >= 300:
            nuevo_rango = "Principiante"
        else:
            nuevo_rango = "Novato"

        if nuevo_rango != rango_anterior:
            store.rango_actual = nuevo_rango
            renpy.notify("¡Nuevo rango alcanzado: " + nuevo_rango + "!")