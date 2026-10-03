# ============================================================
# niveles.rpy
# ============================================================

init python:
    import random

    def crear_enemigos_nivel1():
        enemigos = [
            Guerrero("Goblin", 50, 10, 5, 3, 1, 15, 2, 0, 0, True),
            Mago("Esqueleto Menor", 40, 12, 4, 4, 3, 18, 4, 0, 0, True, 50, 50, 5, 5, 5),
            Arquero("Slime", 30, 8, 3, 3, 4, 10, 6, 0, 0, True, 10, 5),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_nivel2():
        enemigos = [
            Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, 0, 0, 0, True),
            Mago("Mago", 200, 25, 15, 4, 3, 30, 1, 0, 0, True, 100, 100, 10, 10, 10),
            Arquero("Arquero", 120, 25, 12, 4, 4, 30, 2, 0, 0, True, 30, 10),
            Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, 3, 0, 0, True, 100),
            Dragon("Dragon", 300, 60, 30, 2, 3, 70, 4, 0, 0, True, 500, 0, 0),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_nivel3():
        enemigos = [
            Guerrero("Goblin Oscuro", 80, 20, 10, 4, 1, 25, 0, 0, 0, True),
            Arquero("Elfo Corrompido", 100, 22, 12, 4, 4, 28, 1, 0, 0, True, 25, 10),
            Mago("Brujo del Bosque", 120, 20, 10, 3, 3, 35, 2, 0, 0, True, 80, 80, 8, 8, 8),
            Guerrero("Troll", 180, 35, 18, 3, 1, 40, 3, 0, 0, True),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_nivel4():
        enemigos = [
            Guerrero("Guerrero Caido", 160, 38, 22, 4, 1, 38, 0, 0, 0, True),
            Arquero("Arquero Espectral", 130, 28, 14, 4, 4, 32, 1, 0, 0, True, 30, 10),
            Clerigo("Sacerdote Oscuro", 170, 18, 20, 3, 2, 25, 2, 0, 0, True, 150),
            Lich("Lich Menor", 160, 30, 18, 3, 2, 48, 3, 0, 0, True, 250),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_nivel5():
        enemigos = [
            Guerrero("Guardia de Elite", 200, 45, 25, 4, 1, 45, 0, 0, 0, True),
            Arquero("Francotirador", 150, 35, 18, 4, 5, 42, 1, 0, 0, True, 40, 15),
            Mago("Mago de Batalla", 180, 30, 20, 3, 3, 50, 2, 0, 0, True, 200, 200, 15, 15, 15),
            Clerigo("Sanador Imperial", 200, 20, 25, 3, 2, 30, 3, 0, 0, True, 200),
            Dragon("Dragon Rojo", 400, 70, 35, 2, 3, 80, 4, 0, 0, True, 600, 0, 0),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_nivel6():
        enemigos = [
            Lich("Lich Mayor", 250, 40, 25, 3, 3, 60, 0, 0, 0, True, 400),
            Dragon("Dragon Negro", 450, 80, 40, 2, 3, 90, 1, 0, 0, True, 700, 0, 0),
            General("Campeon del Abismo", 450, 65, 45, 3, 2, 75, 2, 0, 0, True, 1200, 600),
            ArchiMago("Archimago Oscuro", 400, 60, 35, 3, 4, 100, 3, 0, 0, True, 1200, 100),
            Mago("Hechicero del Caos", 220, 45, 25, 4, 3, 65, 4, 0, 0, True, 300, 300, 20, 20, 20),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_nivel7():
        enemigos = [
            General("Guardian del Trono", 600, 80, 55, 3, 2, 95, 0, 0, 0, True, 2000, 1000),
            ArchiMago("Archimago Supremo", 500, 75, 45, 3, 4, 120, 1, 0, 0, True, 2000, 200),
            Dragon("Dragon Ancestral", 600, 100, 50, 2, 3, 120, 2, 0, 0, True, 1000, 0, 0),
            Lich("Rey Lich", 400, 60, 40, 3, 3, 90, 3, 0, 0, True, 600),
            Guerrero("Verdugo Real", 500, 90, 50, 4, 1, 110, 5, 0, 0, True),
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    def crear_enemigos_aleatorios(cantidad=8):
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        enemigos = []
        tipos = ["Guerrero", "Mago", "Arquero", "Lich", "Dragon", "General"]
        for i in range(min(cantidad, len(posiciones))):
            x, y = posiciones[i]
            tipo = random.choice(tipos)
            if tipo == "Guerrero":
                enemigos.append(Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, x, y, 0, True))
            elif tipo == "Mago":
                enemigos.append(Mago("Mago", 200, 25, 15, 4, 3, 30, x, y, 0, True, 100, 100, 10, 10, 10))
            elif tipo == "Arquero":
                enemigos.append(Arquero("Arquero", 120, 25, 12, 4, 4, 30, x, y, 0, True, 30, 10))
            elif tipo == "Lich":
                enemigos.append(Lich("Lich", 180, 28, 20, 3, 2, 45, x, y, 0, True, 200))
            elif tipo == "Dragon":
                enemigos.append(Dragon("Dragon", 300, 60, 30, 2, 3, 70, x, y, 0, True, 500, 0, 0))
            elif tipo == "General":
                enemigos.append(General("General", 250, 30, 20, 3, 2, 40, x, y, 0, True, 1000, 500))
        return enemigos

# ============================================================
# LABELS DE NIVELES
# ============================================================

label nivel1:
    $ reproducir_musica("Lvl1.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel1_inicio
    $ enemigos = crear_enemigos_nivel1()
    $ nivel_actual = 1
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel2:
    $ reproducir_musica("Lvl2.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel2_inicio
    $ enemigos = crear_enemigos_nivel2()
    $ nivel_actual = 2
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel3:
    $ reproducir_musica("Lvl3.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel3_inicio
    $ enemigos = crear_enemigos_nivel3()
    $ nivel_actual = 3
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel4:
    $ reproducir_musica("Lvl4.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel4_inicio
    $ enemigos = crear_enemigos_nivel4()
    $ nivel_actual = 4
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel5:
    $ reproducir_musica("Lvl5.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel5_inicio
    $ enemigos = crear_enemigos_nivel5()
    $ nivel_actual = 5
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel6:
    $ reproducir_musica("Lvl6.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel6_inicio
    $ enemigos = crear_enemigos_nivel6()
    $ nivel_actual = 6
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel7:
    $ reproducir_musica("Lvl7.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    call dialogo_nivel7_inicio
    $ enemigos = crear_enemigos_nivel7()
    $ nivel_actual = 7
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel_aleatorio:
    $ reproducir_musica("Lvl1.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    "¡Nivel aleatorio! ¡Preparate para sufrir!"
    $ enemigos = crear_enemigos_aleatorios(8)
    $ nivel_actual = 0
    $ renpy.pause(0.2)
    jump comenzar_batalla