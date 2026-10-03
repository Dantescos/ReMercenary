# ============================================================
# IAs.rpy 
# ============================================================

init python:
    import random

    class IA_Lich:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo):
            try:
                if objeto.get_vida() < objeto.get_vida_max() * 0.3:
                    if objeto.get_magia() >= 40:
                        return objeto.curar()
                    else:
                        return objeto.regenerar_magia()
                if objeto.get_magia() >= 100:
                    return objeto.ataque_masivo(enemigo)
                if objeto.get_magia() >= 50:
                    if objeto.get_vida() < objeto.get_vida_max() * 0.7:
                        return objeto.drenar_vida(enemigo)
                    else:
                        return objeto.ataque_espectral(enemigo)
                if objeto.get_magia() < 30:
                    return objeto.regenerar_magia()
                return objeto.ataque_basico(enemigo)
            except Exception as e:
                print("[IA_Lich ERROR] " + str(e))
                return 0

    class IA_ArchiMago:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo):
            magia = objeto.get_magia()
            x = objeto.get_x()
            y = objeto.get_y()
            try:
                if magia >= 1000:
                    dado = random.randint(1, 12)
                    if dado == 1: objeto.ataque_final(enemigo)
                    elif dado == 2: objeto.ataque_especial(enemigo)
                    elif dado == 3: objeto.ataque_gelido(enemigo)
                    elif dado == 4: objeto.ataque_oscuro(enemigo)
                    elif dado == 5: objeto.ataque_espadas_magicas_de_luz(enemigo)
                    elif dado == 6: objeto.ataque_magico_relampago(enemigo)
                    elif dado == 7: objeto.detener_el_tiempo()
                    elif dado == 8: objeto.ilusion_de_archimago(x, y)
                    elif dado == 9: objeto.magia_de_vuelo(x, y)
                    elif dado == 10: objeto.recuperar_magia(250)
                    elif dado == 11: objeto.ataque_basico(enemigo)
                    else: objeto.curacion_magica()
                elif magia >= 750:
                    dado = random.randint(1, 12)
                    if dado == 1: objeto.ataque_final(enemigo)
                    elif dado == 2: objeto.ataque_especial(enemigo)
                    elif dado == 3: objeto.ataque_gelido(enemigo)
                    elif dado == 4: objeto.ataque_oscuro(enemigo)
                    elif dado == 5: objeto.ataque_espadas_magicas_de_luz(enemigo)
                    elif dado == 6: objeto.ataque_magico_relampago(enemigo)
                    elif dado == 7: objeto.detener_el_tiempo()
                    elif dado == 8: objeto.ilusion_de_archimago(x, y)
                    elif dado == 9: objeto.magia_de_vuelo(x, y)
                    elif dado == 10: objeto.recuperar_magia(250)
                    elif dado == 11: objeto.ataque_basico(enemigo)
                    else: objeto.curacion_magica()
                elif magia >= 500:
                    dado = random.randint(1, 12)
                    if dado == 1: objeto.curacion_magica()
                    elif dado == 2: objeto.ataque_especial(enemigo)
                    elif dado == 3: objeto.ataque_gelido(enemigo)
                    elif dado == 4: objeto.ataque_oscuro(enemigo)
                    elif dado == 5: objeto.ataque_espadas_magicas_de_luz(enemigo)
                    elif dado == 6: objeto.ataque_magico_relampago(enemigo)
                    elif dado == 7: objeto.detener_el_tiempo()
                    elif dado == 8: objeto.ilusion_de_archimago(x, y)
                    elif dado == 9: objeto.magia_de_vuelo(x, y)
                    elif dado == 10: objeto.recuperar_magia(250)
                    elif dado == 11: objeto.ataque_basico(enemigo)
                    else: objeto.curacion_magica()
                else:
                    dado = random.randint(1, 10)
                    if dado == 1: objeto.curacion_magica()
                    elif dado == 2: objeto.ataque_especial(enemigo)
                    elif dado == 3: objeto.ataque_gelido(enemigo)
                    elif dado == 4: objeto.ataque_oscuro(enemigo)
                    elif dado == 5: objeto.ataque_basico(enemigo)
                    elif dado == 6: objeto.ataque_magico_relampago(enemigo)
                    elif dado == 7: objeto.recuperar_magia(250)
                    elif dado == 8: objeto.ilusion_de_archimago(x, y)
                    elif dado == 9: objeto.magia_de_vuelo(x, y)
                    else: objeto.ataque_basico(enemigo)
            except Exception as e:
                print("[IA_ArchiMago ERROR] " + str(e))
                return 0

    class IA_General:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo, aliados=None):
            try:
                energia = objeto.get_energia()
                if energia >= 1000 and objeto.get_cooldown() == 0:
                    dado = random.randint(1, 4)
                    if dado == 1: objeto.canion_especial_final(enemigo)
                    elif dado == 2: objeto.tiro_doble(enemigo)
                    elif dado == 3: objeto.carga_de_caballeria(enemigo, 2)
                    elif dado == 4: objeto.espada(enemigo)
                elif energia < 1000 and objeto.get_cooldown() == 0:
                    dado = random.randint(1, 3)
                    if dado == 1: objeto.tiro_doble(enemigo)
                    elif dado == 2: objeto.carga_de_caballeria(enemigo, 2)
                    elif dado == 3: objeto.espada(enemigo)
            except Exception as e:
                print("[IA_General ERROR] " + str(e))
                return 0

    class IA_Clerigo:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo, aliados):
            try:
                mas_herido = None
                menor_vida = 9999
                for aliado in aliados:
                    if aliado.get_visible() and aliado.get_vida() < aliado.get_vida_max() * 0.5:
                        if aliado.get_vida() < menor_vida:
                            menor_vida = aliado.get_vida()
                            mas_herido = aliado
                if mas_herido is not None and objeto.get_magia() >= 200 and objeto.get_cooldown() == 0:
                    return objeto.sanacion_grupal(mas_herido)
                elif objeto.get_magia() >= 100 and objeto.get_cooldown() == 0:
                    return objeto.palabras_de_fe(enemigo)
                else:
                    return objeto.ataque_basico(enemigo)
            except Exception as e:
                print("[IA_Clerigo ERROR] " + str(e))
                return 0

    class IA_Guerrero:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo):
            try:
                if objeto.get_vida() < objeto.get_vida_max() * 0.3:
                    return objeto.testudo()
                elif random.random() < 0.3:
                    return objeto.arremeter()
                else:
                    return objeto.ataque_basico(enemigo)
            except Exception as e:
                print("[IA_Guerrero ERROR] " + str(e))
                return 0

    class IA_Arquero:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo):
            try:
                if objeto.get_carcaj() <= 1 and objeto.get_flecha_trucada() <= 1:
                    return objeto.recarga_rapida()
                dado = random.randint(1, 10)
                if dado == 1 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.disparar_flechas(enemigo)
                elif dado == 2 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.flecha_de_hielo(enemigo)
                elif dado == 3 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.flecha_venenosa(enemigo)
                elif dado == 4 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.tiro_doble(enemigo)
                elif dado == 5 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.flecha_electrica(enemigo)
                elif dado == 6 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.flecha_explosiva(enemigo)
                elif dado == 7 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.flecha_sombria(enemigo)
                elif dado == 8 and objeto.get_carcaj() > 0 and objeto.get_flecha_trucada() >= 1:
                    return objeto.flechita_especial(enemigo)
                else:
                    return objeto.disparar_flechas(enemigo)
            except Exception as e:
                print("[IA_Arquero ERROR] " + str(e))
                return 0

    class IA_Dragon:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo):
            try:
                magia = objeto.get_magia()
                if objeto.get_escamas_activas() == 0 and magia >= 30:
                    return objeto.escamas_reflectantes()
                if magia >= 200:
                    dado = random.randint(1, 10)
                    if dado <= 4: return objeto.ataque_llamarada_infernal(enemigo)
                    elif dado <= 6: return objeto.ataque_espinas(enemigo)
                    elif dado <= 8 and magia >= 100: return objeto.ataque_luz(enemigo)
                    else: return objeto.ataque_basico(enemigo)
                else:
                    return objeto.ataque_basico(enemigo)
            except Exception as e:
                print("[IA_Dragon ERROR] " + str(e))
                return 0

    class IA_Mago:
        def __init__(self):
            pass

        def evaluar(self, objeto, enemigo):
            try:
                magia = objeto.get_magia()
                vida = objeto.get_vida()
                cooldown = objeto.get_cooldown()

                if vida < 100 and magia >= 290 and cooldown == 0:
                    return objeto.curacion_magica()

                if magia < 200 and cooldown == 0:
                    return objeto.recuperar_magia(250)

                if magia >= 500 and cooldown == 0:
                    dado = random.randint(1, 4)
                    if dado == 1: return objeto.vientos_infernales_prohibidos(enemigo)
                    elif dado == 2: return objeto.ataque_magico_prohibido(enemigo)
                    elif dado == 3: return objeto.ataque_castigo_divino(enemigo)
                    else: return objeto.bola_fuego_mejorada(enemigo)

                if magia >= 200 and magia < 500 and cooldown == 0:
                    dado = random.randint(1, 3)
                    if dado == 1: return objeto.ataque_hielo_infernal(enemigo)
                    elif dado == 2: return objeto.bola_fuego_mejorada(enemigo)
                    else: return objeto.ataque_basico(enemigo)

                return objeto.ataque_basico(enemigo)
            except Exception as e:
                print("[IA_Mago ERROR] " + str(e))
                return 0