# ============================================================
# niveles.rpy
# ============================================================

init python:
    import random

    def equilibrar_enemigos_nivel(enemigos, nivel):
        """Aplica una curva común y conserva diferencias por arquetipo."""
        nivel = max(1, min(7, int(nivel)))
        vida_base = 30 + (nivel - 1) * 13
        ataque_base = 16 + (nivel - 1) * 2
        defensa_base = 3 + (nivel - 1)

        for enemigo in enemigos:
            if isinstance(enemigo, Demonia):
                vida_mult, ataque_mult, defensa_mult = 1.10, 1.15, 1.0
            elif isinstance(enemigo, Dragon):
                vida_mult, ataque_mult, defensa_mult = 1.30, 1.20, 1.15
            elif isinstance(enemigo, General):
                vida_mult, ataque_mult, defensa_mult = 1.15, 1.05, 1.25
            elif isinstance(enemigo, Guerrero):
                vida_mult, ataque_mult, defensa_mult = 1.15, 1.0, 1.20
            elif isinstance(enemigo, Arquero):
                vida_mult, ataque_mult, defensa_mult = 0.80, 1.0, 0.75
            elif isinstance(enemigo, (ArchiMago, Mago)):
                vida_mult, ataque_mult, defensa_mult = 0.85, 1.05, 0.80
            elif isinstance(enemigo, Lich):
                vida_mult, ataque_mult, defensa_mult = 0.90, 1.10, 0.90
            elif isinstance(enemigo, Clerigo):
                vida_mult, ataque_mult, defensa_mult = 0.95, 0.90, 1.0
            else:
                vida_mult, ataque_mult, defensa_mult = 1.0, 1.0, 1.0

            vida = max(1, int(round(vida_base * vida_mult)))
            ataque = max(1, int(round(ataque_base * ataque_mult)))
            defensa = max(0, int(round(defensa_base * defensa_mult)))
            enemigo.set_vida_max(vida)
            enemigo.set_vida(vida)
            enemigo.set_ataque_basico(ataque)
            enemigo.set_defensa(defensa)
            enemigo.set_ataque_especial(max(1, int(round(ataque * 1.25))))

        return enemigos

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
        return equilibrar_enemigos_nivel(enemigos, 1)

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
        return equilibrar_enemigos_nivel(enemigos, 2)

    def crear_enemigos_nivel3():
        enemigos = [
            Guerrero("Goblin Oscuro", 80, 20, 10, 4, 1, 25, 0, 0, 0, True),
            Arquero("Elfo Corrompido", 100, 22, 12, 4, 4, 28, 1, 0, 0, True, 25, 10),
            Mago("Brujo del Bosque", 120, 20, 10, 3, 3, 35, 2, 0, 0, True, 80, 80, 8, 8, 8),
            Guerrero("Troll", 180, 35, 18, 3, 1, 40, 3, 0, 0, True),
            Sacerdotisa(5, 0),   # NUEVA: Sanadora oscura del bosque
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return equilibrar_enemigos_nivel(enemigos, 3)

    def crear_enemigos_nivel4():
        enemigos = [
            Guerrero("Guerrero Caido", 160, 38, 22, 4, 1, 38, 0, 0, 0, True),
            Arquero("Arquero Espectral", 130, 28, 14, 4, 4, 32, 1, 0, 0, True, 30, 10),
            Clerigo("Sacerdote Oscuro", 170, 18, 20, 3, 2, 25, 2, 0, 0, True, 150),
            Lich("Lich Menor", 160, 30, 18, 3, 2, 48, 3, 0, 0, True, 250),
            Licha(5, 0),         # NUEVA: Licha de la cripta
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return equilibrar_enemigos_nivel(enemigos, 4)

    def crear_enemigos_nivel5():
        enemigos = [
            Guerrero("Guardia de Elite", 200, 45, 25, 4, 1, 45, 0, 0, 0, True),
            Arquero("Francotirador", 150, 35, 18, 4, 5, 42, 1, 0, 0, True, 40, 15),
            Mago("Mago de Batalla", 180, 30, 20, 3, 3, 50, 2, 0, 0, True, 200, 200, 15, 15, 15),
            Clerigo("Sanador Imperial", 200, 20, 25, 3, 2, 30, 3, 0, 0, True, 200),
            Dragon("Dragon Rojo", 400, 70, 35, 2, 3, 80, 4, 0, 0, True, 600, 0, 0),
            Demonia(5, 0),       # NUEVA: Demonia al servicio del Imperio
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return equilibrar_enemigos_nivel(enemigos, 5)

    def crear_enemigos_nivel6():
        enemigos = [
            Lich("Lich Mayor", 250, 40, 25, 3, 3, 60, 0, 0, 0, True, 400),
            Dragon("Dragon Negro", 450, 80, 40, 2, 3, 90, 1, 0, 0, True, 700, 0, 0),
            General("Campeon del Abismo", 450, 65, 45, 3, 2, 75, 2, 0, 0, True, 1200, 600),
            ArchiMago("Archimago Oscuro", 400, 60, 35, 3, 4, 100, 3, 0, 0, True, 1200, 100),
            Mago("Hechicero del Caos", 220, 45, 25, 4, 3, 65, 4, 0, 0, True, 300, 300, 20, 20, 20),
            Licha(5, 0),         # NUEVA: Licha del abismo
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return equilibrar_enemigos_nivel(enemigos, 6)

    def crear_enemigos_nivel7():
        enemigos = [
            General("Guardian del Trono", 600, 80, 55, 3, 2, 95, 0, 0, 0, True, 2000, 1000),
            ArchiMago("Archimago Supremo", 500, 75, 45, 3, 4, 120, 1, 0, 0, True, 2000, 200),
            Dragon("Dragon Ancestral", 600, 100, 50, 2, 3, 120, 2, 0, 0, True, 1000, 0, 0),
            Lich("Rey Lich", 400, 60, 40, 3, 3, 90, 3, 0, 0, True, 600),
            Guerrero("Verdugo Real", 500, 90, 50, 4, 1, 110, 5, 0, 0, True),
            Demonia(6, 0),       # NUEVA: Demonia del trono
            Licha(7, 0),         # NUEVA: Licha del trono
            Sacerdotisa(4, 0),   # NUEVA: Sacerdotisa corrupta
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return equilibrar_enemigos_nivel(enemigos, 7)

    def crear_enemigos_aleatorios(cantidad=8):
        # FIX: ahora usa 3 filas [0, 1, 2] = 24 casillas disponibles
        posiciones = [(x, y) for x in range(8) for y in [0, 1, 2]]
        random.shuffle(posiciones)
        enemigos = []
        tipos = ["Guerrero", "Mago", "ArchiMago", "Arquero", "Clerigo","Lich", "Licha", "Demonia", "Dragon", "General", "Sacerdotisa"]
        for i in range(min(cantidad, len(posiciones))):
            x, y = posiciones[i]
            tipo = random.choice(tipos)
            if tipo == "Guerrero":
                enemigos.append(Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, x, y, 0, True))
            elif tipo == "Mago":
                enemigos.append(Mago("Mago", 200, 25, 15, 4, 3, 30, x, y, 0, True, 100, 100, 10, 10, 10))
            elif tipo == "ArchiMago":
                enemigos.append(ArchiMago("Archimago", 300, 35, 25, 3, 3, 50, x, y, 0, True, 1500, 100))
            elif tipo == "Arquero":
                enemigos.append(Arquero("Arquero", 120, 25, 12, 4, 4, 30, x, y, 0, True, 30, 10))
            elif tipo == "Clerigo":
                enemigos.append(Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, x, y, 0, True, 100))
            elif tipo == "Lich":
                enemigos.append(Lich("Lich", 180, 28, 20, 3, 2, 45, x, y, 0, True, 200))
            elif tipo == "Licha":
                enemigos.append(Licha(x, y))
            elif tipo == "Demonia":
                enemigos.append(Demonia(x, y))
            elif tipo == "Dragon":
                enemigos.append(Dragon("Dragon", 300, 60, 30, 2, 3, 70, x, y, 0, True, 500, 0, 0))
            elif tipo == "General":
                enemigos.append(General("General", 250, 30, 20, 3, 2, 40, x, y, 0, True, 1000, 500))
            elif tipo == "Sacerdotisa":
                enemigos.append(Sacerdotisa(x, y))
        return equilibrar_enemigos_nivel(enemigos, 2)

# ============================================================
# LABELS DE NIVELES
# ============================================================

label nivel1:
    $ reproducir_musica("Lvl1.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel1.png"   
    call dialogo_nivel1_inicio from _call_dialogo_nivel1_inicio
    $ enemigos = crear_enemigos_nivel1()
    $ nivel_actual = 1
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel2:
    $ reproducir_musica("Lvl2.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel2.png"    
    call dialogo_nivel2_inicio from _call_dialogo_nivel2_inicio
    $ enemigos = crear_enemigos_nivel2()
    $ nivel_actual = 2
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel3:
    $ reproducir_musica("Lvl3.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel3.png"    
    call dialogo_nivel3_inicio from _call_dialogo_nivel3_inicio
    $ enemigos = crear_enemigos_nivel3()
    $ nivel_actual = 3
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel4:
    $ reproducir_musica("Lvl4.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel4.png"
    call dialogo_nivel4_inicio from _call_dialogo_nivel4_inicio
    $ enemigos = crear_enemigos_nivel4()
    $ nivel_actual = 4
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel5:
    $ reproducir_musica("Lvl5.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel5.png"
    call dialogo_nivel5_inicio from _call_dialogo_nivel5_inicio
    $ enemigos = crear_enemigos_nivel5()
    $ nivel_actual = 5
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel6:
    $ reproducir_musica("Lvl6.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel6.png"  
    call dialogo_nivel6_inicio from _call_dialogo_nivel6_inicio
    $ enemigos = crear_enemigos_nivel6()
    $ nivel_actual = 6
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel7:
    $ reproducir_musica("Lvl7.wav", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel7.png"

    call dialogo_nivel7_inicio from _call_dialogo_nivel7_inicio
    $ enemigos = crear_enemigos_nivel7()
    $ nivel_actual = 7
    $ renpy.pause(0.2)
    jump comenzar_batalla

label nivel_aleatorio:
    $ reproducir_musica("main.mp3", fadein=1.0, loop=True)
    $ boss_musica_activada = False
    $ boss_spawneado = False
    $ tablero_actual = "nivel0.png"
    "¡Nivel aleatorio! ¡Preparate para sufrir!"
    $ cantidad_aleatoria = random.randint(10, 20)
    $ enemigos = crear_enemigos_aleatorios(cantidad_aleatoria)
    $ nivel_actual = 0
    $ renpy.pause(0.2)
    jump comenzar_batalla
