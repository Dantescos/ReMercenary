# ============================================================
# niveles.rpy - Definición de niveles del juego
# ============================================================
init python:
    import random
    def crear_enemigos_nivel1():
        enemigos = [Guerrero("Goblin", 50, 10, 5, 3, 1, 15, 2, 0, 0, True),
            Mago("Esqueleto", 40, 12, 4, 4, 3, 18, 4, 0, 0, True, 50, 5, 5, 5),
            Arquero("Slime", 30, 8, 3, 3, 4, 10, 6, 0, 0, True, 10, 5),
            Guerrero("Orco", 60, 15, 8, 3, 1, 20, 0, 1, 0, True) ]
        # Mezclo las posiciones para que no siempre aparezcan en el mismo lugar
        random.shuffle(enemigos)
        # Asigno posiciones aleatorias dentro de las filas 0 y 1 para Y en el X queda de 0 a 7
        posiciones = [(x, y) for x in range(8) for y in [0, 1]]
        random.shuffle(posiciones)
        for enemigo in enemigos:
            x, y = posiciones.pop()
            enemigo.set_x(x)
            enemigo.set_y(y)
        return enemigos
    def crear_enemigos_nivel2():
            enemigos = [Guerrero("Guerrero", 150, 40, 20, 4, 1, 35, 0, 0, 0, True),
                Mago("Mago", 200, 25, 15, 4, 3, 30, 1, 0, 0, True, 100, 10, 10, 10),
                Arquero("Arquero", 120, 25, 12, 4, 4, 30, 2, 0, 0, True, 30, 10),
                Clerigo("Clerigo", 150, 15, 18, 3, 2, 20, 3, 0, 0, True, 100),
                Dragon("Dragon", 300, 60, 30, 2, 3, 70, 4, 0, 0, True, 500, 0, 0),
                Lich("Lich", 180, 28, 20, 3, 2, 45, 5, 0, 0, True, 200) ]
            # Mezclo las posiciones para que no siempre aparezcan en el mismo lugar
            random.shuffle(enemigos)
            # Asigno posiciones aleatorias dentro de las filas 0 y 1 para Y en el X queda de 0 a 7
            posiciones = [(x, y) for x in range(8) for y in [0, 1]]
            random.shuffle(posiciones)
            for enemigo in enemigos:
                x, y = posiciones.pop()
                enemigo.set_x(x)
                enemigo.set_y(y)
            return enemigos

    def crear_enemigos_aleatorios(cantidad=8): #pongo 8 para que sea fija la cantidad , de paso pruebo
        posiciones = [(x, y) for x in range(8) for y in [0, 1]] # aca estoy  haciendo lo mismo que script , x en el rango de 0 a 7 pero en el y que sea de 0 a 1?
        random.shuffle(posiciones) # mezclo las posiciones
        enemigos = [] # lista vacia para guardar enemigos
        tipos = ["Guerrero", "Mago", "Arquero", "Lich"]
        for i in range(min(cantidad, len(posiciones))): # aca pedi una sugerencia a la IA para hacerla mas compacta esta parte porque no sabia como encararlo sin que me explote..
            x, y = posiciones[i]
            tipo = random.choice(tipos) #mezclo de nuevo
            #Me faltaria el tema de las imagenes de los personajes pero es prueba
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

label nivel1:
    "¡Nivel 1: La invasion de los Goblins!" #Va a ser de prueba
    $ enemigos = crear_enemigos_nivel1()
    $ nivel_actual = 1
    jump comenzar_batalla

label nivel2:
    "¡Nivel 2: La fortaleza enemiga!" # Otro mas de prueba
    $ enemigos = crear_enemigos_nivel2()
    $ nivel_actual = 2
    jump comenzar_batalla

label nivel_aleatorio:
    "¡Nivel aleatorio!" # de paso ya que estaba random quiero probar
    $ enemigos = crear_enemigos_aleatorios(8)
    $ nivel_actual = 0  # 0 aleatorio
    jump comenzar_batalla