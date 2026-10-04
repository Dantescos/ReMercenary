# ============================================================
# Personajes.rpy 
# ============================================================

init python:
    import random

    # ========================================================
    # CLASE BASE
    # ========================================================
    class FichaBase:
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible=True):
            self._clase = clase
            self._vida = vida
            self._vida_max = vida
            self._ataque = ataque
            self._defensa = defensa
            self._punto_mov = punto_mov
            self._rango = rango
            self._danio = danio
            self._x = x
            self._y = y
            self._cooldown = cooldown
            self._visible = visible
            self._magia = 0
            self._magia_max = 0
            self._carcaj = 0
            self._flecha_trucada = 0
            self._energia = 0

        def get_clase(self): return self._clase
        def get_vida(self): return self._vida
        def get_vida_max(self): return self._vida_max
        def get_ataque_basico(self): return self._ataque
        def get_ataque_especial(self): return self._danio
        def get_defensa(self): return self._defensa
        def get_rango(self): return self._rango
        def get_puntos_mov(self): return self._punto_mov
        def get_x(self): return self._x
        def get_y(self): return self._y
        def get_cooldown(self): return self._cooldown
        def get_visible(self): return self._visible
        def get_magia(self): return self._magia
        def get_magia_max(self): return self._magia_max
        def get_carcaj(self): return self._carcaj
        def get_flecha_trucada(self): return self._flecha_trucada
        def get_energia(self): return self._energia

        def set_clase(self, v): self._clase = v
        def set_vida(self, v): self._vida = max(0, v)
        def set_vida_max(self, v): self._vida_max = v
        def set_ataque_basico(self, v): self._ataque = v
        def set_ataque_especial(self, v): self._danio = v
        def set_defensa(self, v): self._defensa = v
        def set_rango(self, v): self._rango = v
        def set_puntos_mov(self, v): self._punto_mov = v
        def set_x(self, v): self._x = v
        def set_y(self, v): self._y = v
        def set_cooldown(self, v): self._cooldown = v
        def set_visible(self, v): self._visible = v

        def set_magia(self, v):
            tope = self._magia_max if self._magia_max > 0 else 9999
            self._magia = max(0, min(int(v), tope))

        def set_magia_max(self, v):
            self._magia_max = max(0, int(v))
            if self._magia > self._magia_max:
                self._magia = self._magia_max

        def set_carcaj(self, v): self._carcaj = max(0, int(v))
        def set_flecha_trucada(self, v): self._flecha_trucada = max(0, int(v))
        def set_energia(self, v): self._energia = max(0, int(v))

        def mover(self, x, y):
            self._x = x
            self._y = y

        def esta_vivo(self):
            return self._vida > 0

        def defenderse_recibir_danio(self, danio_recibido):
            defensa = self.get_defensa() if hasattr(self, 'get_defensa') else 0
            danio_final = max(1, int(danio_recibido - (defensa * 0.5)))
            self._vida = max(0, self._vida - danio_final)
            return danio_final

        def mostrar_info(self):
            renpy.notify("Clase: " + self._clase + " | HP: " + str(self._vida) + " | ATQ: " + str(self._ataque))

    # ========================================================
    # GUERRERO
    # ========================================================
    class Guerrero(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible=True):
            super(Guerrero, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)

        def ataque_basico(self, objetivo=None):
            dano_base = self.get_ataque_basico()
            critico = 0
            if random.randint(1, 100) <= 10:
                critico = dano_base * 1.5
            dano_total = int(dano_base + critico)
            if objetivo is not None:
                return objetivo.defenderse_recibir_danio(dano_total)
            return dano_total

        def testudo(self):
            self.set_defensa(self.get_defensa() * 2)
            return self.get_defensa()

        def arremeter(self):
            self.set_ataque_basico(self.get_ataque_basico() + 20)
            return self.get_ataque_basico()

    # ========================================================
    # MAGO
    # ========================================================
    class Mago(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia, magia_max=0, cantidad_fuego=10, cantidad_carambano=10, cantidad_castigo=10):
            super(Mago, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_magia_max(max(magia, magia_max))
            self.set_magia(magia)
            self.__cantidad_fuego = cantidad_fuego
            self.__cantidad_carambano = cantidad_carambano
            self.__cantidad_castigo = cantidad_castigo

        def ataque_basico(self, objetivo=None):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                if objetivo is not None:
                    return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return self.get_ataque_basico()
            else:
                self.set_magia(self.get_magia() + 50)
                return 0

        def bola_fuego_mejorada(self, objetivo):
            if self.get_magia() >= 200 and self.__cantidad_fuego > 0:
                self.set_magia(self.get_magia() - 200)
                self.__cantidad_fuego -= 1
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_basico() * 1.5))
            return 0

        def ataque_hielo_infernal(self, objetivo):
            if self.get_magia() >= 100 and self.__cantidad_carambano > 0:
                self.set_magia(self.get_magia() - 100)
                self.__cantidad_carambano -= 1
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_basico() * 1.2))
            return 0

        def ataque_castigo_divino(self, objetivo):
            if self.get_magia() >= 300 and self.__cantidad_castigo > 0:
                self.set_magia(self.get_magia() - 300)
                self.__cantidad_castigo -= 1
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_basico() * 2))
            return 0

        def vientos_infernales_prohibidos(self, objetivo):
            if self.get_magia() >= 500:
                self.set_magia(self.get_magia() - 500)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.5))
            return 0

        def ataque_magico_prohibido(self, objetivo):
            if self.get_magia() >= 1000:
                self.set_magia(self.get_magia() - 1000)
                return objetivo.defenderse_recibir_danio(100000)
            return 0

        def proteccion_magica(self):
            if self.get_magia() >= 290:
                self.set_magia(self.get_magia() - 290)
                self.set_defensa(self.get_defensa() * 2)
                return self.get_defensa()
            return 0

        def curacion_magica(self):
            if self.get_vida() < self.get_vida_max() and self.get_magia() >= 290:
                self.set_magia(self.get_magia() - 290)
                curacion = 100
                self.set_vida(self.get_vida() + curacion)
                return curacion
            return 0

        def recuperar_magia(self, cantidad):
            self.set_magia(self.get_magia() + cantidad)
            self.__cantidad_fuego += 5
            self.__cantidad_carambano += 5
            self.__cantidad_castigo += 5
            return self.get_magia()

        def magia_de_vuelo(self, x, y):
            if self.get_magia() >= 150:
                self.set_magia(self.get_magia() - 150)
                self.mover(x, y)
                return True
            return False

    # ========================================================
    # ARCHIMAGO
    # ========================================================
    class ArchiMago(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia, ataque_final=0):
            super(ArchiMago, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_magia_max(magia)
            self.set_magia(magia)
            self.__ataque_final = ataque_final

        def ataque_basico(self, objetivo=None):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                if objetivo is not None:
                    return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return self.get_ataque_basico()
            else:
                self.set_magia(self.get_magia() + 50)
                return 0

        def curacion_magica(self):
            if self.get_vida() < self.get_vida_max() and self.get_magia() >= 290:
                self.set_magia(self.get_magia() - 290)
                curacion = 150
                self.set_vida(self.get_vida() + curacion)
                return curacion
            return 0

        def recuperar_magia(self, cantidad):
            self.set_magia(self.get_magia() + cantidad)
            return self.get_magia()

        def magia_de_vuelo(self, x, y):
            if self.get_magia() >= 200:
                self.set_magia(self.get_magia() - 200)
                self.mover(x, y)
                return True
            return False

        def ataque_especial(self, objetivo):
            if self.get_magia() >= 300:
                self.set_magia(self.get_magia() - 300)
                return objetivo.defenderse_recibir_danio(self.get_ataque_especial())
            return 0

        def ataque_gelido(self, objetivo):
            if self.get_magia() >= 259:
                self.set_magia(self.get_magia() - 259)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.2))
            return 0

        def ataque_oscuro(self, objetivo):
            if self.get_magia() >= 360:
                self.set_magia(self.get_magia() - 360)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.3))
            return 0

        def ataque_espadas_magicas_de_luz(self, objetivo):
            if self.get_magia() >= 500:
                self.set_magia(self.get_magia() - 500)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.5))
            return 0

        def ataque_magico_relampago(self, objetivo):
            if self.get_magia() >= 365:
                self.set_magia(self.get_magia() - 365)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.4))
            return 0

        def ataque_final(self, objetivo):
            if self.get_magia() >= 1000:
                self.set_magia(self.get_magia() - 1000)
                return objetivo.defenderse_recibir_danio(100000)
            return 0

        def sabiduria_ancestral(self):
            self.set_magia(self.get_magia() + 300)
            return self.get_magia()

        def detener_el_tiempo(self):
            if self.get_magia() >= 800:
                self.set_magia(self.get_magia() - 800)
                return True
            return False

        def ilusion_de_archimago(self, x, y):
            if self.get_magia() >= 390:
                self.set_magia(self.get_magia() - 390)
                return True
            return False

    # ========================================================
    # ARQUERO
    # ========================================================
    class Arquero(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, carcaj, flecha_trucada):
            super(Arquero, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_carcaj(carcaj)
            self.set_flecha_trucada(flecha_trucada)

        def disparar_flechas(self, objetivo):
            if self.get_carcaj() >= 1:
                self.set_carcaj(self.get_carcaj() - 1)
                return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
            return 0

        def flechita_especial(self, objetivo):
            if self.get_flecha_trucada() >= 1 and self.get_carcaj() >= 1:
                self.set_carcaj(self.get_carcaj() - 1)
                self.set_flecha_trucada(self.get_flecha_trucada() - 1)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.5))
            return 0

        def recarga_rapida(self):
            self.set_carcaj(30)
            self.set_flecha_trucada(10)
            return True

        def flecha_de_hielo(self, objetivo):
            if self.get_flecha_trucada() >= 1 and self.get_carcaj() >= 1:
                self.set_carcaj(self.get_carcaj() - 1)
                self.set_flecha_trucada(self.get_flecha_trucada() - 1)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 2.0))
            return 0

        def flecha_venenosa(self, objetivo):
            if self.get_flecha_trucada() >= 1 and self.get_carcaj() >= 1:
                self.set_carcaj(self.get_carcaj() - 1)
                self.set_flecha_trucada(self.get_flecha_trucada() - 1)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 3.0))
            return 0

        def flecha_explosiva(self, objetivo):
            if self.get_flecha_trucada() >= 1 and self.get_carcaj() >= 1:
                self.set_carcaj(self.get_carcaj() - 1)
                self.set_flecha_trucada(self.get_flecha_trucada() - 1)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 4.0))
            return 0

        def flecha_electrica(self, objetivo):
            if self.get_flecha_trucada() >= 1 and self.get_carcaj() >= 1:
                self.set_carcaj(self.get_carcaj() - 1)
                self.set_flecha_trucada(self.get_flecha_trucada() - 1)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 5.0))
            return 0

        def flecha_sombria(self, objetivo):
            return self.flecha_venenosa(objetivo)

        def tiro_doble(self, objetivo):
            if self.get_flecha_trucada() >= 2 and self.get_carcaj() >= 2:
                self.set_carcaj(self.get_carcaj() - 2)
                self.set_flecha_trucada(self.get_flecha_trucada() - 2)
                d1 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                d2 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return d1 + d2
            return 0

    # ========================================================
    # LICH
    # ========================================================
    class Lich(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia):
            super(Lich, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_magia_max(magia)
            self.set_magia(magia)

        def ataque_basico(self, objetivo=None):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                if objetivo is not None:
                    return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return self.get_ataque_basico()
            else:
                self.set_magia(self.get_magia() + 50)
                return 0

        def ataque_espectral(self, objetivo):
            if self.get_magia() >= 50:
                self.set_magia(self.get_magia() - 50)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_basico() * 1.3))
            return 0

        def drenar_vida(self, objetivo):
            if self.get_magia() >= 30:
                self.set_magia(self.get_magia() - 30)
                danio = objetivo.defenderse_recibir_danio(self.get_ataque_basico() + 10)
                robo = int(danio * 0.5)
                self.set_vida(self.get_vida() + robo)
                return danio
            return 0

        def ataque_masivo(self, objetivo):
            if self.get_magia() >= 100:
                danio_base = int(self.get_magia() * 1.5) + self.get_ataque_basico()
                self.set_magia(0)
                return objetivo.defenderse_recibir_danio(danio_base)
            return 0

        def curar(self):
            if self.get_magia() >= 40:
                self.set_magia(self.get_magia() - 40)
                curacion = int(self.get_vida_max() * 0.15) + 20
                self.set_vida(self.get_vida() + curacion)
                return curacion
            return 0

        def regenerar_magia(self):
            restauracion = int(self.get_magia_max() * 0.1) + 20
            self.set_magia(self.get_magia() + restauracion)
            return restauracion

    # ========================================================
    # CLERIGO
    # ========================================================
    class Clerigo(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia):
            super(Clerigo, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_magia_max(magia)
            self.set_magia(magia)

        def ataque_basico(self, objetivo=None):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                if objetivo is not None:
                    return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return self.get_ataque_basico()
            else:
                self.set_magia(self.get_magia() + 50)
                return 0

        def sanacion_grupal(self, aliado):
            if self.get_magia() >= 200:
                self.set_magia(self.get_magia() - 200)
                aliado.set_vida(aliado.get_vida() + 80)
                return 80
            return 0

        def palabras_de_fe(self, enemigo):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                enemigo.set_ataque_basico(int(enemigo.get_ataque_basico() * 0.6))
                return True
            return False

        def luz_cegadora_dia(self, enemigo):
            if self.get_magia() >= 300:
                self.set_magia(self.get_magia() - 300)
                return enemigo.defenderse_recibir_danio(int(self.get_ataque_especial() * 2.5))
            return 0

        def exorcismo(self, enemigo):
            if self.get_magia() >= 400:
                self.set_magia(self.get_magia() - 400)
                return enemigo.defenderse_recibir_danio(int(self.get_ataque_especial() * 3.5))
            return 0

        def escudo_de_fe_magico(self):
            if self.get_magia() >= 200:
                self.set_magia(self.get_magia() - 200)
                self.set_defensa(self.get_defensa() + 1000)
                return self.get_defensa()
            return 0

        def mi_fe_es_inquebrantable(self, objetivo):
            if self.get_magia() >= 1000:
                self.set_magia(self.get_magia() - 1000)
                return objetivo.defenderse_recibir_danio(10000)
            return 0

        def recuperacion_sagrada(self, cantidad):
            self.set_magia(self.get_magia() + cantidad)
            return self.get_magia()

    # ========================================================
    # GENERAL
    # ========================================================
    class General(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, energia, ataque_final=0):
            super(General, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_energia(energia)
            self.__ataque_final = ataque_final

        def ataque_basico(self, objetivo=None):
            if objetivo is not None:
                return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
            return self.get_ataque_basico()

        def espada(self, objetivo):
            if self.get_energia() >= 100:
                self.set_energia(self.get_energia() - 100)
                return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
            else:
                self.set_energia(self.get_energia() + 200)
                return 0

        def canon_de_mano(self, objetivo):
            if self.get_energia() >= 250:
                self.set_energia(self.get_energia() - 250)
                return objetivo.defenderse_recibir_danio(self.get_ataque_especial())
            return 0

        def tiro_doble(self, objetivo):
            if self.get_energia() >= 350:
                self.set_energia(self.get_energia() - 350)
                d1 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                d2 = objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return d1 + d2
            return 0

        def carga_de_caballeria(self, objetivo, casillas=0):
            if casillas >= 2:
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_basico() * 1.5))
            return objetivo.defenderse_recibir_danio(self.get_ataque_basico())

        def canion_especial_final(self, objetivo):
            if self.get_energia() >= 1000:
                self.set_energia(self.get_energia() - 1000)
                return objetivo.defenderse_recibir_danio(100000)
            return 0

    # ========================================================
    # DRAGON
    # ========================================================
    class Dragon(FichaBase):
        def __init__(self, clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible, magia, espinas=0, escamas_activas=0):
            super(Dragon, self).__init__(clase, vida, ataque, defensa, punto_mov, rango, danio, x, y, cooldown, visible)
            self.set_magia_max(magia)
            self.set_magia(magia)
            self.__espinas = espinas
            self.__escamas_activas = escamas_activas

        def get_espinas(self): return self.__espinas
        def set_espinas(self, v): self.__espinas = v
        def get_escamas_activas(self): return self.__escamas_activas
        def set_escamas_activas(self, v): self.__escamas_activas = v

        def ataque_basico(self, objetivo=None):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                if objetivo is not None:
                    return objetivo.defenderse_recibir_danio(self.get_ataque_basico())
                return self.get_ataque_basico()
            else:
                self.set_magia(self.get_magia() + 50)
                return 0

        def ataque_llamarada_infernal(self, objetivo):
            if self.get_magia() >= 200:
                self.set_magia(self.get_magia() - 200)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 2.0))
            return 0

        def ataque_espinas(self, objetivo):
            if self.get_magia() >= 100:
                self.set_magia(self.get_magia() - 100)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 1.5))
            return 0

        def ataque_luz(self, objetivo):
            if self.get_magia() >= 150:
                self.set_magia(self.get_magia() - 150)
                return objetivo.defenderse_recibir_danio(int(self.get_ataque_especial() * 2.2))
            return 0

        def escamas_reflectantes(self):
            if self.get_magia() >= 30:
                self.set_magia(self.get_magia() - 30)
                self.__escamas_activas = 2
                return True
            return False

        def regeneracion_dragon(self):
            restauracion = int(self.get_vida_max() * 0.1)
            self.set_vida(self.get_vida() + restauracion)
            return restauracion

        def recuperacion_draconica(self, cantidad):
            self.set_magia(self.get_magia() + cantidad)
            return self.get_magia()

    # ========================================================
    # HEROES JUGABLES - STATS BALANCEADOS
    # ========================================================
    class Kazuki(Mago):
        def __init__(self, x, y):
            # HP 1500 | ATK 250 | DEF 100 | daño esp 250 | magia 500/5000
            super(Kazuki, self).__init__("Kazuki", 1500, 250, 100, 4, 3, 250, x, y, 0, True, 500, 5000, 20, 20, 20)

        def potenciar_aliado(self, aliado=None):
            if aliado is None:
                aliado = self
            nuevo = int(aliado.get_ataque_basico() * 1.2)
            aliado.set_ataque_basico(nuevo)
            return nuevo

    class Lyra(Arquero):
        def __init__(self, x, y):
            # HP 1200 | ATK 250 | DEF 90 | daño esp 250 | carcaj 80 | esp 40
            super(Lyra, self).__init__("Lyra", 1200, 250, 90, 5, 4, 250, x, y, 0, True, 80, 40)

        def flecha_perforante(self, objetivo):
            danio_base = self.get_ataque_basico() + 10
            defensa_objetivo = int(objetivo.get_defensa() * 0.5)
            danio = max(1, danio_base - defensa_objetivo)
            objetivo.defenderse_recibir_danio(danio)
            return danio

    class Gromm(Guerrero):
        def __init__(self, x, y):
            # HP 3000 | ATK 200 | DEF 220 | daño esp 200 (tanque)
            super(Gromm, self).__init__("Gromm", 3000, 200, 220, 3, 1, 200, x, y, 0, True)

        def escudo_levantado(self):
            self.set_defensa(self.get_defensa() * 2)
            return self.get_defensa()