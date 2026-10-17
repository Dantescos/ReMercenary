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
    import random
    def es_boss(clase):
        return clase in NOMBRES_BOSSES

    def obtener_imagen_enemigo(clase):
        if es_boss(clase):
            for nombre_boss, imagen in IMAGENES_BOSSES.items():
                if nombre_boss == clase:
                    return imagen

        imagenes_comunes = {
            "Kazuki": "Kazuki.png",
            "Lyra": "Lyra.png",
            "Gromm": "Gromm.png",
            "Dragon": "Dragon.png",
            # Licha debe ir antes que Lich: el nombre "Licha" contiene "Lich".
            "Licha": "Licha.png",
            "Lich": "Lich.png",
            "Archimago": "Archimago.png",
            "Mago": "Mago.png",
            "Clerigo": "Clerigo.png",
            "Guerrero": "Guerrero.png",
            "General": "General.png",
            "Arquero": "Arquero.png",
            "Sacerdotisa": "Sacerdotisa.png",
            "Demonia": "Demonia.png",
            "Morgana": "Mago.png",
        }
        for tipo, imagen in imagenes_comunes.items():
            if tipo in clase:
                return imagen

        return "default.png"

    def obtener_imagen_retrato(clase):
        return "images/" + obtener_imagen_enemigo(clase)

    # Los nombres de sprites de combate no son uniformes en todos los archivos.
    # Resolverlos de forma segura evita errores de archivo inexistente.
    def obtener_sprite_combate(clase, accion="idle"):
        import os
        import renpy

        base = obtener_imagen_enemigo(clase)
        nombre = base[:-4] if base.lower().endswith(".png") else base
        # El retrato del Dragon usa "Dragon.png", pero sus poses se guardaron
        # con el nombre femenino "dragona". Mapearlo evita mostrar el retrato
        # estático durante todo el combate.
        aliases_sprites = {
            "Dragon": "dragona",
        }
        for tipo, alias in aliases_sprites.items():
            if tipo in clase:
                nombre = alias
                break
        sufijos = {
            "idle": ["_idle", ""],
            "ataque": ["_ataque", "_ataca", "_ataue", "_dile", ""],
            "dano": ["_recibe_dano", "_redibe_dano", "_recibe_ataque", "_dano", ""],
        }
        # Sprites propios de personajes de la historia.
        especiales = {
            "Kazuki": {"ataque": "Kazuki_ataca.png", "dano": "Kazuki_redibe_dano.png"},
            "Gromm": {"ataque": "Gromm_ataca.png"},
            "Lyra": {},
        }
        carpeta = os.path.join(renpy.config.gamedir, "images")
        candidatos = []
        if clase in especiales and accion in especiales[clase]:
            candidatos.append(especiales[clase][accion])
        candidatos.extend(nombre + sufijo + ".png" for sufijo in sufijos.get(accion, [""]))
        for archivo in candidatos:
            ruta = os.path.join(carpeta, archivo)
            if os.path.isfile(ruta):
                return "images/" + archivo
        return "images/" + base

    def fraccion_vida(personaje):
        maxima = max(1, personaje.get_vida_max())
        return max(0.0, min(1.0, float(personaje.get_vida()) / maxima))

    def fraccion_magia(personaje):
        maxima = max(1, personaje.get_magia_max())
        return max(0.0, min(1.0, float(personaje.get_magia()) / maxima))

    def formato_recurso_combate(valor):
        valor = int(valor)
        if valor >= 1000:
            miles = valor / 1000.0
            return ("%.1fk" % miles).replace(".0k", "k")
        return str(valor)

    def restaurar_recursos_combate(*personajes):
        for personaje in personajes:
            if personaje is None or not personaje.esta_vivo():
                continue
            personaje.set_vida(personaje.get_vida_max())
            maxima_magia = personaje.get_magia_max()
            if maxima_magia > 0:
                personaje.set_magia(maxima_magia)

    # ========================================================
    # PROGRESION DE JEFES
    # ========================================================

    def crear_boss_nivel1(x, y):
        return Guerrero("Ogro", 1500, 160, 40, 3, 1, 200, x, y, 0, True)

    def crear_boss_nivel2(x, y):
        return Mago("Esqueleto", 2200, 180, 55, 3, 2, 250, x, y, 0, True, 800, 800, 15, 15, 15)

    def crear_boss_nivel3(x, y):
        return Guerrero("Traidor", 3200, 200, 75, 3, 1, 300, x, y, 0, True)

    def crear_boss_nivel4(x, y):
        return General("Caballero Corrompido", 4200, 220, 95, 3, 1, 340, x, y, 0, True, 2500, 1200)

    def crear_boss_nivel5(x, y):
        return ArchiMago("Senor Oscuro Humano", 5400, 240, 115, 3, 3, 410, x, y, 0, True, 3000, 1000)

    def crear_boss_nivel6(x, y):
        return Dragon("Senor Oscuro Demonio", 7000, 260, 140, 3, 3, 490, x, y, 0, True, 4000, 0, 0)

    def crear_boss_nivel7(x, y):
        return Dragon("Senor Oscuro Tentaculos", 8500, 280, 165, 4, 4, 580, x, y, 0, True, 6000, 0, 0)

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

# ========================================================
# JEFE ALEATORIO (para nivel aleatorio)
# ========================================================
    def crear_boss_aleatorio(x, y):
        opciones = [crear_boss_nivel1,
            crear_boss_nivel2,
            crear_boss_nivel3,
            crear_boss_nivel4,
            crear_boss_nivel5,]
        funcion_elegida = random.choice(opciones)
        return funcion_elegida(x, y)
