# ============================================================
# bosses.rpy - Stats de los 7 jefes (progresión balanceada)
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

    # ========================================================
    # PROGRESIÓN DE JEFES
    # Ogro/Esqueleto = fáciles (duran 4-6 turnos)
    # Traidor/Caballero = medios
    # Señor Oscuro (3 formas) = muy duros
    # ========================================================

    def crear_boss_nivel1(x, y):
        # OGRO (fácil): 1500 HP, 60 ATK, 40 DEF, 75 daño
        return Guerrero("Ogro", 1500, 60, 40, 3, 1, 75, x, y, 0, True)

    def crear_boss_nivel2(x, y):
        # ESQUELETO (fácil-medio): 2500 HP, 80 ATK, 55 DEF, 100 daño
        return Mago("Esqueleto", 2500, 80, 55, 3, 2, 100, x, y, 0, True, 800, 800, 15, 15, 15)

    def crear_boss_nivel3(x, y):
        # TRAIDOR (medio): 4000 HP, 100 ATK, 75 DEF, 135 daño
        return Guerrero("Traidor", 4000, 100, 75, 3, 1, 135, x, y, 0, True)

    def crear_boss_nivel4(x, y):
        # CABALLERO CORROMPIDO (medio-duro): 6000 HP, 125 ATK, 95 DEF, 170 daño
        return General("Caballero Corrompido", 6000, 125, 95, 3, 1, 170, x, y, 0, True, 2500, 1200)

    def crear_boss_nivel5(x, y):
        # SEÑOR OSCURO - FORMA 1 HUMANO (duro): 8000 HP, 150 ATK, 115 DEF, 205 daño
        return ArchiMago("Senor Oscuro Humano", 8000, 150, 115, 3, 3, 205, x, y, 0, True, 3000, 1000)

    def crear_boss_nivel6(x, y):
        # SEÑOR OSCURO - FORMA 2 DEMONIO (muy duro): 11000 HP, 175 ATK, 140 DEF, 245 daño
        return Dragon("Senor Oscuro Demonio", 11000, 175, 140, 3, 3, 245, x, y, 0, True, 4000, 0, 0)

    def crear_boss_nivel7(x, y):
        # SEÑOR OSCURO - FORMA 3 TENTÁCULOS (extremo): 16000 HP, 205 ATK, 165 DEF, 290 daño
        return Dragon("Senor Oscuro Tentaculos", 16000, 205, 165, 4, 4, 290, x, y, 0, True, 6000, 0, 0)

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