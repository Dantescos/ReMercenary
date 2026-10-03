# ============================================================
# logros.rpy - Sistema de logros y rangos
# ============================================================

default enemigos_muertos_total = 0
default rango_actual = "Novato"
default habilidades_usadas = 0
default bosses_matados = 0
default niveles_completados = 0
default logros_desbloqueados = {}

init python:
    LOGROS = {
        # Primeros pasos
        "primer_sangre":       ("Primera Sangre", "Mataste a tu primer enemigo"),
        "primer_boss":         ("Cazador de Jefes", "Derrotaste a tu primer jefe"),
        "primer_nivel":        ("Superviviente", "Completaste el Nivel 1"),
        "primer_heroe":        ("Héroe Legendario", "Usaste una habilidad especial por primera vez"),

        # Niveles completados
        "nivel_1":             ("Nivel 1 Completado", "Sobreviviste a La Invasion de los Goblins"),
        "nivel_2":             ("Nivel 2 Completado", "Descansaste en la Cripta Olvidada"),
        "nivel_3":             ("Nivel 3 Completado", "Cruzaste el Bosque de las Sombras"),
        "nivel_4":             ("Nivel 4 Completado", "Profanaste el Templo de los Caidos"),
        "nivel_5":             ("Nivel 5 Completado", "Asaltaste la Fortaleza del General"),
        "nivel_6":             ("Nivel 6 Completado", "Descendiste al Abismo de los Condenados"),
        "nivel_7":             ("Nivel 7 Completado", "Llegaste al Trono del Senor Oscuro"),
        "todos_niveles":       ("Conquistador", "Completaste todos los niveles"),

        # Bosses
        "boss_1":              ("Verdugo de Goblins", "Derrotaste al Ogro Berserker"),
        "boss_2":              ("Exterminador", "Derrotaste al Dragon de la Cripta"),
        "boss_3":              ("Domador de Bestias", "Derrotaste al Wyvern del Bosque"),
        "boss_4":              ("Purificador", "Derrotaste al General Caido"),
        "boss_5":              ("Rompe-Fortalezas", "Derrotaste al General Oscuro"),
        "boss_6":              ("Azote del Abismo", "Derrotaste al Archimago Oscuro"),
        "boss_7":              ("Salvador de Veridia", "Derrotaste al Senor Oscuro"),
        "todos_bosses":        ("Matadioses", "Derrotaste a TODOS los jefes del juego"),

        # Cantidad de enemigos
        "matar_10":            ("Aprendiz de Combate", "Mataste 10 enemigos"),
        "matar_25":            ("Veterano", "Mataste 25 enemigos"),
        "matar_50":            ("Guerrero", "Mataste 50 enemigos"),
        "matar_100":           ("Carnicero", "Mataste 100 enemigos"),
        "matar_200":           ("Devorador", "Mataste 200 enemigos"),
        "matar_500":           ("Ángel de la Muerte", "Mataste 500 enemigos"),

        # Habilidades
        "habilidad_5":         ("Tactico", "Usaste 5 habilidades especiales"),
        "habilidad_15":        ("Estratega", "Usaste 15 habilidades especiales"),
        "habilidad_30":        ("Maestro de Habilidades", "Usaste 30 habilidades especiales"),

        # Rangos
        "rango_principiante":  ("Principiante", "Alcanzaste el rango Principiante (300 enemigos)"),
        "rango_maestro":       ("Maestro", "Alcanzaste el rango Maestro (600 enemigos)"),
        "rango_experto":       ("Experto", "Alcanzaste el rango Experto (1000 enemigos)"),
        "rango_leyenda":       ("Leyenda", "Alcanzaste el rango Leyenda (2000 enemigos)"),

        # Finales
        "final_bueno":         ("Final Bueno", "Kazuki se quedo en Veridia"),
        "final_malo":          ("Final Malo", "Kazuki cayo en batalla"),
        "final_isekai":        ("Regreso a Casa", "Kazuki desperto en el hospital"),
        "final_overlord":      ("Overlord", "Kazuki se convirtio en el nuevo Senor Oscuro"),
        "todos_finales":       ("Coleccionista de Finales", "Viste todos los finales del juego"),

        # Desafíos
        "sin_morir_1":         ("Intocable", "Completaste un nivel sin perder ningun heroe"),
        "velocidad":           ("Flash", "Mataste a un jefe en 10 turnos o menos"),
        "ejercito_lleno":      ("General Supremo", "Desplegaste 8 unidades en un nivel"),
        "todos_heroes":        ("Los Tres Mosqueteros", "Ganaste con Kazuki, Lyra y Gromm"),
    }

    def desbloquear_logro(nombre):
        if nombre not in store.logros_desbloqueados:
            store.logros_desbloqueados[nombre] = True
            if nombre in LOGROS:
                titulo, descripcion = LOGROS[nombre]
                renpy.notify("LOGRO: " + titulo)

    def logro_esta_desbloqueado(nombre):
        return nombre in store.logros_desbloqueados

    def registrar_muerte_enemigo():
        store.enemigos_muertos_total += 1
        # Logros por cantidad
        if store.enemigos_muertos_total == 1:
            desbloquear_logro("primer_sangre")
        if store.enemigos_muertos_total == 10:
            desbloquear_logro("matar_10")
        if store.enemigos_muertos_total == 25:
            desbloquear_logro("matar_25")
        if store.enemigos_muertos_total == 50:
            desbloquear_logro("matar_50")
        if store.enemigos_muertos_total == 100:
            desbloquear_logro("matar_100")
        if store.enemigos_muertos_total == 200:
            desbloquear_logro("matar_200")
        if store.enemigos_muertos_total == 500:
            desbloquear_logro("matar_500")
        verificar_rango()

    def registrar_habilidad_usada():
        store.habilidades_usadas += 1
        if store.habilidades_usadas == 1:
            desbloquear_logro("primer_heroe")
        if store.habilidades_usadas == 5:
            desbloquear_logro("habilidad_5")
        if store.habilidades_usadas == 15:
            desbloquear_logro("habilidad_15")
        if store.habilidades_usadas == 30:
            desbloquear_logro("habilidad_30")

    def registrar_boss_matado(numero_boss):
        store.bosses_matados += 1
        if store.bosses_matados == 1:
            desbloquear_logro("primer_boss")
        if numero_boss >= 1 and numero_boss <= 7:
            desbloquear_logro("boss_" + str(numero_boss))
        if store.bosses_matados >= 7:
            desbloquear_logro("todos_bosses")

    def registrar_nivel_completado(numero_nivel):
        store.niveles_completados += 1
        if numero_nivel == 1:
            desbloquear_logro("primer_nivel")
        if numero_nivel >= 1 and numero_nivel <= 7:
            desbloquear_logro("nivel_" + str(numero_nivel))
        if store.niveles_completados >= 7:
            desbloquear_logro("todos_niveles")

    def verificar_rango():
        total = store.enemigos_muertos_total
        rango_anterior = store.rango_actual
        if total >= 2000:
            nuevo_rango = "Leyenda"
            desbloquear_logro("rango_leyenda")
        elif total >= 1000:
            nuevo_rango = "Experto"
            desbloquear_logro("rango_experto")
        elif total >= 600:
            nuevo_rango = "Maestro"
            desbloquear_logro("rango_maestro")
        elif total >= 300:
            nuevo_rango = "Principiante"
            desbloquear_logro("rango_principiante")
        else:
            nuevo_rango = "Novato"

        if nuevo_rango != rango_anterior:
            store.rango_actual = nuevo_rango
            renpy.notify("¡Nuevo rango alcanzado: " + nuevo_rango + "!")


# ============================================================
# SCREEN: PANTALLA DE LOGROS
# ============================================================
screen pantalla_logros():
    modal True
    tag menu

    frame:
        xfill True
        yfill True
        background "#0a0a1a"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        text "LOGROS" size 60 color "#ffcc00" bold True xalign 0.5
        text "Desbloqueados: [len(logros_desbloqueados)] / [len(LOGROS)]" size 30 color "#ffffff" xalign 0.5
        null height 20

        viewport:
            xsize 1600
            ysize 800
            scrollbars "vertical"
            mousewheel True

            vbox:
                spacing 8
                for clave in sorted(LOGROS.keys()):
                    $ titulo, descripcion = LOGROS[clave]
                    $ desbloqueado = logro_esta_desbloqueado(clave)
                    $ color_fondo = "#1a1a2a" if desbloqueado else "#0a0a12"
                    $ color_titulo = "#ffffff" if desbloqueado else "#555555"
                    $ color_desc = "#aaaaaa" if desbloqueado else "#333333"
                    $ icono = "✓" if desbloqueado else "·"
                    $ color_icono = "#00ff00" if desbloqueado else "#333333"

                    frame:
                        xsize 1500
                        background color_fondo
                        padding (15, 10)
                        hbox:
                            spacing 15
                            text "[icono]" size 30 color color_icono
                            vbox:
                                text titulo size 25 color color_titulo bold True
                                text descripcion size 18 color color_desc

        null height 15
        textbutton "Cerrar":
            action Return()
            text_size 30
            xalign 0.5