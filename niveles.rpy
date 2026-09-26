# ============================================================
# niveles.rpy - Definición de niveles del juego
# ============================================================

init python:
    import random
    
    # ========================================================
    # NIVEL 1: LA INVASION DE LOS GOBLINS
    # ========================================================
    # Enemigos: 4 unidades basicas (goblin, esqueleto, slime, orco)
    # Dificultad: Facil
    # Objetivo: Eliminar a todos los enemigos
    # ========================================================
    def crear_enemigos_nivel1():
        enemigos = [
            Guerrero("Goblin", 50, 10, 5, 3, 1, 15, 2, 0, 0, True),
            Mago("Esqueleto", 40, 12, 4, 4, 3, 18, 4, 0, 0, True, 50, 5, 5, 5),
            Arquero("Slime", 30, 8, 3, 3, 4, 10, 6, 0, 0, True, 10, 5),
            Guerrero("Orco", 60, 15, 8, 3, 1, 20, 0, 1, 0, True)
        ]
        # Mezclo las posiciones para que no siempre aparezcan en el mismo lugar
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    # ========================================================
    # NIVEL 2: LA FORTALEZA ENEMIGA
    # ========================================================
    # Enemigos: 6 unidades variadas (incluye jefe: Dragon)
    # Dificultad: Media
    # Objetivo: Eliminar a todos los enemigos
    # ========================================================
    def crear_enemigos_nivel2():
        enemigos = [
            Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, 0, 0, 0, True),
            Mago("Mago", 200, 25, 15, 4, 3, 30, 1, 0, 0, True, 100, 10, 10, 10),
            Arquero("Arquero", 120, 25, 12, 4, 4, 30, 2, 0, 0, True, 30, 10),
            Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, 3, 0, 0, True, 100),
            Dragon("Dragon", 300, 60, 30, 2, 3, 70, 4, 0, 0, True, 500, 0, 0),
            Lich("Lich", 180, 28, 20, 3, 2, 45, 5, 0, 0, True, 200)
        ]
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos

    # ========================================================
    # NIVEL ALEATORIO
    # ========================================================
    # Enemigos: 8 aleatorios
    # Dificultad: Variable
    # Objetivo: Eliminar a todos los enemigos
    # ========================================================
    def crear_enemigos_aleatorios(cantidad=8):
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        enemigos = []
        tipos = ["Guerrero", "Mago", "Arquero", "Lich"]
        for i in range(min(cantidad, len(posiciones))):
            x, y = posiciones[i]
            tipo = random.choice(tipos)
            if tipo == "Guerrero":
                enemigos.append(Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, x, y, 0, True))
            elif tipo == "Mago":
                enemigos.append(Mago("Mago", 200, 25, 15, 4, 3, 30, x, y, 0, True, 100, 10, 10, 10))
            elif tipo == "Arquero":
                enemigos.append(Arquero("Arquero", 120, 25, 12, 4, 4, 30, x, y, 0, True, 30, 10))
            elif tipo == "Lich":
                enemigos.append(Lich("Lich", 180, 28, 20, 3, 2, 45, x, y, 0, True, 200))
        return enemigos

# ============================================================
# LABELS DE NIVELES
# ============================================================

# ============================================================
# NIVEL 1: LA INVASION DE LOS GOBLINS
# ============================================================
label nivel1:
    # --- LORE: DIALOGO DE INICIO ---
    call dialogo_nivel1_inicio
    
    # --- MECANICA: CREAR ENEMIGOS ---
    "¡Nivel 1: La invasion de los Goblins!"
    $ enemigos = crear_enemigos_nivel1()
    $ nivel_actual = 1
    
    # --- IR A LA BATALLA ---
    jump comenzar_batalla

# ============================================================
# NIVEL 2: LA FORTALEZA ENEMIGA
# ============================================================
label nivel2:
    # --- LORE: DIALOGO DE INICIO ---
    "¡Nivel 2: La fortaleza enemiga!"
    "Despues de salvar la aldea, Kazuki y Lyra se dirigen a la fortaleza."
    "Pero lo que encontraran ahi... nadie lo esperaba."
    
    # --- MECANICA: CREAR ENEMIGOS ---
    $ enemigos = crear_enemigos_nivel2()
    $ nivel_actual = 2
    
    # --- IR A LA BATALLA ---
    jump comenzar_batalla

# ============================================================
# NIVEL ALEATORIO
# ============================================================
label nivel_aleatorio:
    "¡Nivel aleatorio!"
    $ enemigos = crear_enemigos_aleatorios(8)
    $ nivel_actual = 0
    
    jump comenzar_batalla