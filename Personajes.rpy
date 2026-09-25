init python:
    class FichaBase:
            def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible=True):
                self.__clase = clase
                self.__vida = vida
                self.__ataque = ataque
                self.__defensa = defensa
                self.__punto_mov = punto_mov
                self.__rango = rango
                self.__danio = danio
                self.__x = x
                self.__y = y
                self.__cooldown = cooldown
                self.__visible = visible

            # GETTERS 
            def get_ataque_basico(self):
                return self.__ataque

            def get_ataque_especial(self):
                return self.__danio

            def get_vida(self):
                return self.__vida

            def get_rango(self):
                return self.__rango

            def get_clase(self):
                return self.__clase

            def get_puntos_mov(self):
                return self.__punto_mov

            def get_cooldown(self):
                return self.__cooldown

            def get_x(self):
                return self.__x

            def get_y(self):
                return self.__y

            def get_visible(self):
                return self.__visible

            def get_defensa(self):
                return self.__defensa

            # SETTERS 
            def set_visible(self, visible):
                self.__visible = visible

            def set_cooldown(self, cooldown):
                self.__cooldown = cooldown

            def set_vida(self, vida):
                self.__vida = vida

            def set_ataque_basico(self, ataque):
                self.__ataque = ataque

            def set_ataque_especial(self, danio):
                self.__danio = danio

            def set_puntos_mov(self, mov):
                self.__punto_mov = mov

            def set_defensa(self, defensa):
                self.__defensa = defensa

            def set_x(self, x):
                self.__x = x

            def set_y(self, y):
                self.__y = y

            def mover(self, x, y):
                self.__x = x
                self.__y = y

            def defenderse_recibir_danio(self, danio_recibido):
                danio_final = danio_recibido - self.__defensa
                if danio_final < 0:
                    danio_final = 0
                self.__vida -= danio_final
                if self.__vida < 0:
                    self.__vida = 0
                return danio_final

            def esta_vivo(self):
                return self.__vida > 0

            def mostrar_info(self):
                print("Clase: " + self.__clase + ", HP: " + str(self.__vida) + ", ATQ: " + str(self.__ataque) + ", DEF: " + str(self.__defensa) + ", MOV: " + str(self.__punto_mov))

    class Dragon(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia, espinas, escamas_activas):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_vida(int(self.get_vida() * 1.5))
            self.set_ataque_basico(int(self.get_ataque_basico() * 1.5))
            self.set_ataque_especial(int(self.get_ataque_especial() * 1.5))
            self.__magia = magia
            self.__espinas = espinas
            self.__escamas_activas = escamas_activas

        def get_magia(self): return self.__magia

        def set_magia(self, magia):self.__magia = magia

        def get_espinas(self):return self.__espinas

        def set_espinas(self, espinas):self.__espinas = espinas

        def get_escamas_activas(self):return self.__escamas_activas

        def set_escamas_activas(self, escamas):self.__escamas_activas = escamas

        def ataque_basico(self,objetivo):
            if self.__magia>100:
                self.__magia -=100
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Golpe draconico! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.set_vida(self.get_vida() - 100)
                print("No hay magia. Perdes vida. HP: " + str(self.get_vida()))
                return 0
        def ataque_llamarada_infernal(self, objetivo):
            if self.__magia >= 200:
                self.__magia -= 200
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Llamarada infernal! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.set_vida(self.get_vida() - 100)
                print("No hay magia. Perdes vida. HP: " + str(self.get_vida()))
                return 0
        def ataque_espinas(self, objetivo):
            if self.__magia >= 200:
                self.__magia -= 200
                danio_espinas = int(self.get_vida() * 0.1)
                danio_final = objetivo.defenderse_recibir_danio(danio_espinas)
                print("Ataque de espinas! Danio: " + str(danio_final))
                return danio_final
            else:
                self.set_vida(self.get_vida() - 200)
                print("No hay magia. Perdes vida. HP: " + str(self.get_vida()))
                return 0
        def ataque_luz(self, objetivo):
            if self.__magia >= 100:
                self.__magia -= 100
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Rayo de luz! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.set_vida(self.get_vida() - 200)
                self.__magia += 250
                print("Sin magia. Recarga pero te atacan.")
                return 0
        def vuelo_dragon(self, x, y):
            if self.__magia >= 300:
                self.__magia -= 300
                self.mover(x, y)
                print("Dragon vuela a (" + str(x) + ", " + str(y) + "). Magia: " + str(self.__magia))
                return True
            else:
                print("Sin magia para volar.")
                return False
        def escamas_reflectantes(self):
            if self.__magia >= 30:
                self.__magia -= 30
                self.__escamas_activas = 2
                print("Escamas reflectantes activadas (2 turnos).")
                return True
            else:
                self.set_vida(self.get_vida() - 20)
                print("Sin magia. Perdes vida.")
                return False
        def recibir_danio(self, danio_recibido, objetivo=None):
            danio_a_vida = self.defenderse_recibir_danio(danio_recibido)
            if self.__escamas_activas > 0 and objetivo is not None:
                danio_reflejado = int(danio_recibido * 0.3)
                print("Escamas reflejan " + str(danio_reflejado) + " de danio.")
                objetivo.defenderse_recibir_danio(danio_reflejado)
            return danio_a_vida
        def regeneracion_dragon(self):
            if self.get_vida() > 0:
                restauracion = int(self.get_vida() * 0.1)
                self.set_vida(self.get_vida() + restauracion)
                print("Regeneracion: +" + str(restauracion) + " HP.")
                return True
            return False
        def recuperacion_draconica(self, cantidad):
            if self.__magia + cantidad <= 1000 and self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__magia += cantidad
                print("Recuperacion de magia. Magia: " + str(self.__magia))
                return True
            else:
                print("No se pudo recuperar.")
                return False

    class General(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, energia, ataque_final):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__energia = energia
            self.__ataque_final = ataque_final

        def get_energia(self):return self.__energia
        def set_energia(self, energia):self.__energia = energia
        def potenciador_cercano(self, aliado):
            if abs(self.get_x() - aliado.get_x()) <= 3 and abs(self.get_y() - aliado.get_y()) <= 3:
                nuevo_ataque = aliado.get_ataque_basico() * 2.05
                aliado.set_ataque_basico(nuevo_ataque)
                print("Potenciador cercano: " + aliado.get_clase() + " ATQ +105%")
                return nuevo_ataque
            else:
                print("Demasiado lejos.")
                return aliado.get_ataque_basico()
        def potenciador_lejano(self, aliado):
            if abs(self.get_x() - aliado.get_x()) <= 8 and abs(self.get_y() - aliado.get_y()) <= 8:
                nuevo_ataque = aliado.get_ataque_basico() * 1.05
                aliado.set_ataque_basico(nuevo_ataque)
                print("Potenciador lejano: " + aliado.get_clase() + " ATQ +5%")
                return nuevo_ataque
            else:
                print("Demasiado lejos.")
                return aliado.get_ataque_basico()
        def espada(self, objetivo):
            if self.__energia >= 100:
                self.__energia -= 100
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Corte mortal! Danio: " + str(danio) + ", Energia: " + str(self.__energia))
                return danio
            else:
                self.__energia += 250
                print("Sin energia. Recarga pero te atacan.")
                return 0
        def canon_de_mano(self, objetivo):
            if self.__energia >= 250:
                self.__energia -= 250
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial())
                print("Canon de mano! Danio: " + str(danio) + ", Energia: " + str(self.__energia))
                return danio
            else:
                self.__energia += 250
                print("Sin energia. Recarga pero te atacan.")
                return 0

        def canion_especial_final(self, objetivo):
            if self.__energia >= 1000 and self.get_cooldown() == 0:
                self.__energia -= 1000
                self.__ataque_final = 100000
                self.set_cooldown(5)
                danio = objetivo.defenderse_recibir_danio(self.__ataque_final)
                print("Canion final! Danio: " + str(danio))
                return danio
            else:
                self.__energia += 250
                self.set_cooldown(3)
                print("Sin energia o cooldown. Recarga.")
                return 0

        def carga_de_caballeria(self, objetivo, casillas_movidas):
            if casillas_movidas >= 2:
                danio_extra = self.get_ataque_basico() * 1.5
                print("Carga de caballeria! +50% danio por moverte " + str(casillas_movidas) + " casillas")
                danio = objetivo.defenderse_recibir_danio(danio_extra)
            else:
                print("Ataque normal.")
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
            return danio

        def tiro_doble(self, objetivo):
            if self.__energia >= 350:
                self.__energia -= 350
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio1 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                    danio2 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                    danio_total = danio1 + danio2
                    print("Tiro doble! Danio total: " + str(danio_total))
                    return danio_total
                else:
                    print("Fuera de rango.")
                    return 0
            else:
                print("Sin energia.")
                return 0

    class Mago(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia, magia_max=None, cantidad_fuego=10, cantidad_carambano=10, cantidad_castigo=10):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__magia = magia
            if magia_max is None:
                magia_max = magia
            self.__magia_max = magia_max
            self.__cantidad_fuego = cantidad_fuego
            self.__cantidad_carambano = cantidad_carambano
            self.__cantidad_castigo = cantidad_castigo
            self.__ataque_final = 0

        def get_magia(self):
            return self.__magia

        def set_magia(self, magia):
            self.__magia = magia

        def ataque_basico(self, objetivo):
            if self.__magia >= 100:
                self.__magia -= 100
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Ragnarok! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.__magia += 250
                print("Sin magia. Recarga pero te atacan.")
                return 0

        def bola_fuego_mejorada(self, objetivo):
            if self.__magia >= 200 and self.__cantidad_fuego > 0:
                self.__magia -= 200
                self.__cantidad_fuego -= 1
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico() * 1.5)
                print("Bola de fuego mejorada! Danio: " + str(danio) + ", Fuego restante: " + str(self.__cantidad_fuego))
                return danio
            else:
                self.__magia += 250
                print("Sin magia o sin bolas de fuego.")
                return 0

        def ataque_hielo_infernal(self, objetivo):
            if self.__magia >= 100 and self.__cantidad_carambano > 0:
                self.__magia -= 100
                self.__cantidad_carambano -= 1
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico() * 1.2)
                print("Hielo infernal! Danio: " + str(danio) + ", Carambanos: " + str(self.__cantidad_carambano))
                return danio
            else:
                self.__magia += 250
                print("Sin magia o sin carambanos.")
                return 0

        def ataque_castigo_divino(self, objetivo):
            if self.__magia >= 300 and self.__cantidad_castigo > 0:
                self.__magia -= 300
                self.__cantidad_castigo -= 1
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico() * 2)
                print("Castigo divino! Danio: " + str(danio) + ", Castigos: " + str(self.__cantidad_castigo))
                return danio
            else:
                self.__magia += 250
                print("Sin magia o sin castigos.")
                return 0

        def vientos_infernales_prohibidos(self, objetivo):
            if self.__magia >= 500 and self.get_cooldown() == 0:
                self.__magia -= 500
                self.set_cooldown(3)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 1.5)
                print("Vientos infernales! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.__magia += 250
                self.set_cooldown(3)
                print("Sin magia o en cooldown.")
                return 0

        def ataque_magico_prohibido(self, objetivo):
            if self.__magia >= 1000 and self.get_cooldown() == 0:
                self.__magia -= 1000
                self.__ataque_final = 100000
                self.set_cooldown(10)
                print("Hechizo prohibido: Waldgose! Magia restante: " + str(self.__magia))
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial())
                return danio
            else:
                self.__magia += 250
                self.set_cooldown(5)
                print("Sin magia o cooldown.")
                return 0

        def proteccion_magica(self):
            if self.__magia >= 290 and self.get_cooldown() == 0:
                self.__magia -= 290
                self.set_cooldown(2)
                self.set_defensa(self.get_defensa() * 2)
                print("Escudo magico activado. Defensa: " + str(self.get_defensa()))
                return self.get_defensa()
            else:
                self.__magia += 250
                print("Sin magia o cooldown.")
                return 0

        def curacion_magica(self):
            if self.get_vida() < 400 and self.__magia >= 290 and self.get_cooldown() == 0:
                self.__magia -= 290
                self.set_cooldown(3)
                curacion = 300
                self.set_vida(min(self.get_vida() + curacion, 400))
                print("Curacion magica! HP: " + str(self.get_vida()))
                return self.get_vida()
            else:
                self.__magia += 250
                print("Sin magia o cooldown.")
                return 0

        def recuperar_magia(self, cantidad):
            if self.__magia + cantidad <= 1000 and self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__magia += cantidad
                self.__cantidad_fuego += 10
                self.__cantidad_carambano += 10
                self.__cantidad_castigo += 10
                print("Recuperacion de magia. Magia: " + str(self.__magia))
                return True
            else:
                print("No se pudo recuperar.")
                return False

        def magia_de_vuelo(self, x, y):
            if self.__magia >= 150 and self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__magia -= 150
                self.mover(x, y)
                print("Magia de vuelo! Magia: " + str(self.__magia))
                return True
            else:
                print("Sin magia o cooldown.")
                return False

    class Guerrero(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__dano = danio

        def ataque_basico(self, objetivo=None):
            dano_base = self.get_ataque_basico() - self.get_defensa()
            dano_diferencial = dano_base + self.diferencia_de_dano()
            dano_total = int(dano_diferencial + self.chance_de_critico())
            print("Ataque basico: " + str(dano_total))
            if objetivo:
                objetivo.defenderse_recibir_danio(dano_total)
            return danio_total

        def testudo(self):
            self.set_defensa(self.get_defensa() * 2)
            print("Testudo activado. Defensa: " + str(self.get_defensa()))
            return self.get_defensa()

        def arremeter(self):
            self.set_ataque_basico(self.get_ataque_basico() + 20)
            print("Arremeter. Ataque: " + str(self.get_ataque_basico()))
            return self.get_ataque_basico()

        def diferencia_de_dano(self):
            variable = random.randint(-20, 20)
            dano_extra = self.__dano * (variable / 100)
            return round(self.__dano + dano_extra)

        def chance_de_critico(self):
            if random.randint(1, 100) <= 10:
                return self.__dano * 2.5
            return 0

    class Arquero(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, carcaj, flecha_trucada):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__carcaj = carcaj
            self.__flecha_trucada = flecha_trucada

        def get_carcaj(self):
            return self.__carcaj

        def set_carcaj(self, carcaj):
            self.__carcaj = carcaj

        def get_flecha_trucada(self):
            return self.__flecha_trucada

        def set_flecha_trucada(self, flecha):
            self.__flecha_trucada = flecha

        def disparar_flechas(self, objetivo):
            if self.__carcaj >= 1:
                self.__carcaj -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                    print("Flecha disparada. Danio: " + str(danio) + ", Flechas: " + str(self.__carcaj))
                    return danio
                else:
                    print("Fuera de rango.")
                    return 0
            else:
                print("Sin flechas.")
                return 0

        def flechita_especial(self, objetivo):
            if self.__flecha_trucada >= 1 and self.__carcaj >= 1:
                self.__carcaj -= 1
                self.__flecha_trucada -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 1.5)
                    print("Flecha especial! Danio: " + str(danio) + ", Flechas trucadas: " + str(self.__flecha_trucada))
                    return danio
                else:
                    print("Fuera de rango.")
                    return 0
            else:
                print("Sin flechas especiales.")
                return 0

        def recarga_rapida(self):
            if self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__carcaj = 30
                self.__flecha_trucada = 10
                print("Recarga rapida. Flechas restauradas.")
                return True
            else:
                print("En cooldown.")
                return False

        def flecha_de_hielo(self, objetivo):
            if self.__flecha_trucada >= 1 and self.__carcaj >= 1:
                self.__carcaj -= 1
                self.__flecha_trucada -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 2.0)
                    print("Flecha de hielo! Danio: " + str(danio))
                    return danio
            return 0

        def flecha_venenosa(self, objetivo):
            if self.__flecha_trucada >= 1 and self.__carcaj >= 1:
                self.__carcaj -= 1
                self.__flecha_trucada -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 3.0)
                    print("Flecha venenosa! Danio: " + str(danio))
                    return danio
            return 0

        def flecha_explosiva(self, objetivo):
            if self.__flecha_trucada >= 1 and self.__carcaj >= 1:
                self.__carcaj -= 1
                self.__flecha_trucada -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 10.5)
                    print("Flecha explosiva! Danio: " + str(danio))
                    return danio
            return 0

        def flecha_sombria(self, objetivo):
            if self.__flecha_trucada >= 1 and self.__carcaj >= 1:
                self.__flecha_trucada -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 30.0)
                    print("Flecha sombria! Danio: " + str(danio))
                    return danio
            return 0

        def tiro_doble(self, objetivo):
            if self.__flecha_trucada >= 2 and self.__carcaj >= 2:
                self.__carcaj -= 2
                self.__flecha_trucada -= 2
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio1 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                    danio2 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                    print("Tiro doble! Danio total: " + str(danio1 + danio2))
                    return danio1 + danio2
            return 0

        def flecha_electrica(self, objetivo):
            if self.__flecha_trucada >= 1 and self.__carcaj >= 1:
                self.__carcaj -= 1
                self.__flecha_trucada -= 1
                if abs(self.get_x() - objetivo.get_x()) <= self.get_rango() and abs(self.get_y() - objetivo.get_y()) <= self.get_rango():
                    danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 25.0)
                    print("Flecha electrica! Danio: " + str(danio))
                    return danio
            return 0

    class Lich(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__magia = magia
            self.__magia_max = magia
            self.__vida_max = vida

        def get_magia(self):
            return self.__magia

        def set_magia(self, magia):
            self.__magia = magia

        def get_vida_max(self):
            return self.__vida_max

        def ataque_basico(self, objetivo=None):
            print("Orbe de sombras! Danio: " + str(self.get_ataque_basico()))
            if objetivo:
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return danio
            return self.get_ataque_basico()

        def ataque_espectral(self, objetivo):
            if self.__magia >= 50:
                self.__magia -= 50
                danio_base = self.get_ataque_basico() + int(self.__magia * 0.2)
                danio = objetivo.defenderse_recibir_danio(danio_base)
                print("Ataque espectral! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                print("Sin magia para ataque espectral.")
                return 0

        def drenar_vida(self, objetivo):
            if self.__magia >= 30:
                self.__magia -= 30
                danio = self.get_ataque_basico() + 10
                danio = objetivo.defenderse_recibir_danio(danio)
                robo = int(danio * 0.5)
                self.set_vida(min(self.__vida_max, self.get_vida() + robo))
                print("Drenar vida! Danio: " + str(danio) + ", roba " + str(robo) + " HP. Vida Lich: " + str(self.get_vida()))
                return danio
            else:
                print("Sin magia para drenar vida.")
                return 0

        def ataque_masivo(self, objetivo):
            if self.__magia >= 100:
                danio_base = int(self.__magia * 1.5) + self.get_ataque_basico()
                self.__magia = 0
                danio = objetivo.defenderse_recibir_danio(danio_base)
                print("Ataque masivo! Danio: " + str(danio) + " (magia agotada)")
                return danio
            else:
                print("No hay suficiente magia para ataque masivo.")
                return 0

        def curar(self):
            if self.__magia >= 40:
                self.__magia -= 40
                curacion = int(self.get_vida() * 0.15) + 20
                self.set_vida(min(self.__vida_max, self.get_vida() + curacion))
                print("Lich se cura " + str(curacion) + " HP. Vida: " + str(self.get_vida()))
                return curacion
            else:
                print("Sin magia para curarse.")
                return 0

        def regenerar_magia(self):
            if self.__magia < self.__magia_max:
                restauracion = int(self.__magia_max * 0.1)
                self.__magia = min(self.__magia_max, self.__magia + restauracion)
                print("Lich regenera " + str(restauracion) + " de magia. Magia: " + str(self.__magia))
                return restauracion
            return 0

        def defenderse(self, danio_bruto=None):
            if danio_bruto is not None:
                return self.defenderse_recibir_danio(danio_bruto)
            else:
                print(self.get_clase() + " se defiende!")
                return 0

        def levantar_muertos(self):
            """Habilidad de invocación (Placeholder)."""
            print("El Lich levanta muertos! (Placeholder)")
            return True

    class Clerigo(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__magia = magia

        def get_magia(self):
            return self.__magia

        def set_magia(self, magia):
            self.__magia = magia


        def ataque_basico(self, objetivo):
            if self.__magia >= 100:
                self.__magia -= 100
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Bendicion sangrada! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.__magia += 250
                print("Sin magia. Recarga pero te atacan.")
                return 0

        def sanacion_grupal(self, aliado):
            if self.__magia >= 200 and self.get_cooldown() == 0:
                if abs(self.get_x() - aliado.get_x()) <= 2 and abs(self.get_y() - aliado.get_y()) <= 2:
                    self.__magia -= 200
                    self.set_cooldown(2)
                    nueva_vida = aliado.get_vida() * 1.5
                    aliado.set_vida(nueva_vida)
                    print("Sanacion grupal. " + aliado.get_clase() + " HP: " + str(nueva_vida))
                    return nueva_vida
            print("No se pudo sanar.")
            return 0

        def luz_cegadora_dia(self, enemigo):
            if self.__magia >= 300 and self.get_cooldown() == 0:
                self.__magia -= 300
                self.set_cooldown(3)
                if enemigo.get_clase() in ["No muerto", "Lich", "Demonio", "Senor Oscuro"]:
                    danio = enemigo.defenderse_recibir_danio(self.get_ataque_especial() * 3.5)
                else:
                    danio = enemigo.defenderse_recibir_danio(self.get_ataque_especial())
                print("Luz cegadora! Danio: " + str(danio))
                return danio
            return 0

        def exorcismo(self, enemigo):
            if self.__magia >= 400 and self.get_cooldown() == 0:
                self.__magia -= 400
                self.set_cooldown(5)
                if enemigo.get_clase() in ["No muerto", "Lich", "Demonio", "Senor Oscuro"]:
                    danio = enemigo.defenderse_recibir_danio(self.get_ataque_especial() * 4.5)
                else:
                    danio = enemigo.defenderse_recibir_danio(self.get_ataque_especial())
                print("Exorcismo! Danio: " + str(danio))
                return danio
            return 0

        def palabras_de_fe(self, objetivo):
            if self.__magia >= 100 and self.get_cooldown() == 0:
                self.__magia -= 100
                self.set_cooldown(3)
                if objetivo.get_clase() in ["No muerto", "Lich", "Demonio", "Senor Oscuro"]:
                    objetivo.set_ataque_basico(objetivo.get_ataque_basico() * 0.90)
                else:
                    objetivo.set_ataque_basico(objetivo.get_ataque_basico() * 0.40)
                print("Palabras de fe. Ataque de " + objetivo.get_clase() + " reducido.")
                return True
            return False

        def escudo_de_fe_magico(self):
            """Eleva drásticamente la defensa del clérigo."""
            if self.__magia >= 200 and self.get_cooldown() == 0:
                self.__magia -= 200
                self.set_defensa(self.get_defensa() + 1000)
                print("Escudo de fe. Defensa: " + str(self.get_defensa()))
                return self.get_defensa()
            else:
                print("Sin magia o cooldown.")
                return 0

        def mi_fe_es_inquebrantable(self, objetivo):
            if self.__magia >= 1000 and self.get_cooldown() == 0:
                self.__magia -= 1000
                self.set_cooldown(10)
                self.set_vida(self.get_vida() * 0.5)
                danio = objetivo.defenderse_recibir_danio(10000)
                print("Fe inquebrantable! Danio: " + str(danio))
                return danio
            else:
                print("Sin magia o cooldown.")
                return 0

        def recuperacion_sagrada(self, cantidad):
            if self.__magia + cantidad <= 1000 and self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__magia += cantidad
                print("Recuperacion de magia. Magia: " + str(self.__magia))
                return True
            else:
                print("No se pudo recuperar.")
                return False

    class ArchiMago(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia, ataque_final):
            super().__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.__magia = magia
            self.__vida_max = vida
            self.__ataque_final = ataque_final

        def get_magia(self):
            return self.__magia

        def set_magia(self, magia):
            self.__magia = magia

        def ataque_basico(self, objetivo):
            if self.__magia >= 100:
                self.__magia -= 100
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                print("Vollzanbel! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.__magia += 250
                print("Sin magia. Recarga.")
                return 0

        def curacion_magica(self):
            if self.get_vida() < self.__vida_max and self.__magia >= 290 and self.get_cooldown() == 0:
                self.__magia -= 290
                self.set_cooldown(3)
                curacion = 300
                self.set_vida(min(self.get_vida() + curacion, self.__vida_max))
                print("Curacion magica. HP: " + str(self.get_vida()))
                return self.get_vida()
            else:
                print("No se puede curar.")
                return 0

        def recuperar_magia(self, cantidad):
            if self.__magia + cantidad <= 1000 and self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__magia += cantidad
                print("Recuperacion de magia. Magia: " + str(self.__magia))
                return True
            else:
                print("No se pudo recuperar.")
                return False

        def magia_de_vuelo(self, x, y):
            if self.__magia >= 200 and self.get_cooldown() == 0:
                self.set_cooldown(2)
                self.__magia -= 150
                self.mover(x, y)
                print("Magia de vuelo. Magia: " + str(self.__magia))
                return True
            else:
                print("Sin magia o cooldown.")
                return False

        def ataque_especial(self, objetivo):
            if self.__magia >= 300 and self.get_cooldown() == 0:
                self.__magia -= 300
                self.set_cooldown(2)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial())
                print("Doom! Danio: " + str(danio) + ", Magia: " + str(self.__magia))
                return danio
            else:
                self.__magia += 250
                print("Sin magia o cooldown.")
                return 0

        def ataque_gelido(self, objetivo):
            if self.__magia >= 259 and self.get_cooldown() == 0:
                self.__magia -= 259
                self.set_cooldown(2)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 1.2)
                print("Todlicher Winter! Danio: " + str(danio))
                return danio
            else:
                return 0

        def ataque_oscuro(self, objetivo):
            if self.__magia >= 360 and self.get_cooldown() == 0:
                self.__magia -= 360
                self.set_cooldown(2)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 1.3)
                print("Ewige Finsternis! Danio: " + str(danio))
                return danio
            else:
                return 0

        def ataque_espadas_magicas_de_luz(self, objetivo):
            if self.__magia >= 500 and self.get_cooldown() == 0:
                self.__magia -= 500
                self.set_cooldown(3)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 1.5)
                print("Catastravia! Danio: " + str(danio))
                return danio
            else:
                return 0

        def ataque_magico_relampago(self, objetivo):
            if self.__magia >= 365 and self.get_cooldown() == 0:
                self.__magia -= 365
                self.set_cooldown(2)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_especial() * 1.4)
                print("Judradjim! Danio: " + str(danio))
                return danio
            else:
                return 0

        def ataque_final(self, objetivo):
            if self.__magia >= 1000 and self.get_cooldown() == 0:
                self.__magia -= 1000
                self.set_cooldown(10)
                danio = objetivo.defenderse_recibir_danio(10000000)
                print("ULTIMATE ZOOLTRAAK! Danio: " + str(danio))
                return danio
            else:
                self.__magia += 250
                print("Sin magia o cooldown.")
                return 0

        def sabiduria_ancestral(self):
            if self.get_cooldown() == 0:
                self.set_cooldown(4)
                self.__magia += 300
                print("Sabiduria ancestral. Magia: " + str(self.__magia))
                return self.__magia
            else:
                print("En cooldown.")
                return 0

        def detener_el_tiempo(self):
            if self.__magia >= 800 and self.get_cooldown() == 0:
                self.__magia -= 800
                self.set_cooldown(5)
                self.set_vida(self.get_vida() - 200)
                print("DETENER EL TIEMPO!")
                return True
            else:
                self.set_cooldown(5)
                self.set_vida(self.get_vida() - 250)
                print("Fallo al detener el tiempo.")
                return False

        def ilusion_de_archimago(self, x, y):
            if self.__magia >= 390 and self.get_cooldown() == 0:
                self.__magia -= 390
                self.set_cooldown(3)
                print("Ilusion de Archimago activada.")
                return True
            else:
                print("Fallo.")
                return False

    class Kazuki(Mago):
        def __init__(self, x, y):
            super().__init__("Kazuki", 180, 25, 20, 4, 3, 35, x, y, 0, True, 100, 250, 10, 10, 10)

        def potenciar_aliado(self, aliado=None):
            """Potencia el ataque de un aliado o de sí mismo."""
            if aliado is None:
                aliado = self
            nuevo_ataque = int(aliado.get_ataque_basico() * 1.2)
            aliado.set_ataque_basico(nuevo_ataque)
            print("Kazuki potencia a " + aliado.get_clase() + "! ATQ +20%.")
            return nuevo_ataque

    class Lyra(Arquero):
        def __init__(self, x, y):
            super().__init__("Lyra", 140, 28, 15, 5, 4, 35, x, y, 0, True, 30, 10)

        def flecha_perforante(self, objetivo):
            danio_base = self.get_ataque_basico() + 10
            defensa_objetivo = int(objetivo.get_defensa() * 0.5)
            danio = max(1, danio_base - defensa_objetivo)
            objetivo.defenderse_recibir_danio(danio)
            print("Lyra dispara flecha perforante! Danio: " + str(danio))
            return danio

    class Gromm(Guerrero):
        def __init__(self, x, y):
            super().__init__("Gromm", 220, 30, 40, 3, 1, 40, x, y, 0, True)

        def escudo_levantado(self):
            """Duplica la defensa del enano."""
            self.set_defensa(self.get_defensa() * 2)
            print("Gromm levanta su escudo! Defensa: " + str(self.get_defensa()))
            return self.get_defensa()