# ============================================================
# bosses.rpy
# ============================================================

define NOMBRES_BOSSES = [
    "Ogro",
    "Esqueleto",
    "Traidor",
    "Caballero Corrompido",
    "Senor Oscuro Humano",
    "Senor Oscuro Demonio",
    "Senor Oscuro Tentaculos",
]

define IMAGENES_BOSSES = {
    "Ogro": "boss1.png",
    "Esqueleto": "boss2.png",
    "Traidor": "boss3.png",
    "Caballero Corrompido": "boss4.png",
    "Senor Oscuro Humano": "boss5.png",
    "Senor Oscuro Demonio": "boss6.png",
    "Senor Oscuro Tentaculos": "boss7.png",
}

init python:
    def es_boss(clase):
        return clase in NOMBRES_BOSSES

    def obtener_imagen_enemigo(clase):
        if es_boss(clase):
            for nombre_boss, imagen in IMAGENES_BOSSES.items():
                if nombre_boss == clase:
                    return imagen

        imagenes_comunes = {
            "Dragon": "Dragon.png",
            "Lich": "Lich.png",
            "Archimago": "Archimago.png",
            "Mago": "Mago.png",
            "Clerigo": "Clerigo.png",
            "Guerrero": "Guerrero.png",
            "General": "General.png",
            "Arquero": "Arquero.png",
        }
        for tipo, imagen in imagenes_comunes.items():
            if tipo in clase:
                return imagen

        return "default.png"

    def crear_boss_nivel1(x, y):
        return Guerrero("Ogro", 200, 30, 15, 3, 1, 35, x, y, 0, True)

    def crear_boss_nivel2(x, y):
        return Mago("Esqueleto", 300, 40, 25, 3, 2, 60, x, y, 0, True, 400, 400, 15, 15, 15)

    def crear_boss_nivel3(x, y):
        return Guerrero("Traidor", 350, 55, 35, 3, 1, 70, x, y, 0, True)

    def crear_boss_nivel4(x, y):
        return General("Caballero Corrompido", 500, 65, 50, 3, 1, 80, x, y, 0, True, 1500, 500)

    def crear_boss_nivel5(x, y):
        return ArchiMago("Senor Oscuro Humano", 600, 70, 55, 3, 3, 90, x, y, 0, True, 1800, 400)

    def crear_boss_nivel6(x, y):
        return Dragon("Senor Oscuro Demonio", 800, 110, 65, 3, 3, 120, x, y, 0, True, 2500, 0, 0)

    def crear_boss_nivel7(x, y):
        return Dragon("Senor Oscuro Tentaculos", 1500, 150, 90, 4, 4, 250, x, y, 0, True, 4000, 0, 0)

    def crear_boss_por_nivel(nivel, x, y):
        if nivel == 1:
            return crear_boss_nivel1(x, y)
        elif nivel == 2:
            return crear_boss_nivel2(x, y)
        elif nivel == 3:
            return crear_boss_nivel3(x, y)
        elif nivel == 4:
            return crear_boss_nivel4(x, y)
        elif nivel == 5:
            return crear_boss_nivel5(x, y)
        elif nivel == 6:
            return crear_boss_nivel6(x, y)
        elif nivel == 7:
            return crear_boss_nivel7(x, y)
        return None