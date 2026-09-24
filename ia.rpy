init python:
    class IA_Lich:
        def __init__(self):
            pass
        def evaluar_vida_magia(self, objeto, enemigo):
            if objeto.get_vida() < objeto.get_vida_max() * 0.3:
                if objeto.get_magia() >= 40:
                    print("Lich esta muy herido! Se cura.")
                    return objeto.curar()
                else:
                    print("Lich herido sin magia. Regenera.")
                    return objeto.regenerar_magia()
            if objeto.get_magia() >= 100:
                print("Lich usa ataque masivo!")
                return objeto.ataque_masivo(enemigo)
            if objeto.get_magia() >= 50:
                if objeto.get_vida() < objeto.get_vida_max() * 0.7:
                    print("Lich drena vida para recuperarse.")
                    return objeto.drenar_vida(enemigo) if hasattr(objeto, "drenar_vida") else objeto.ataque_espectral(enemigo)
                else:
                    print("Lich usa ataque espectral.")
                    return objeto.ataque_espectral(enemigo)
            if objeto.get_magia() < 30:
                print("Lich regenera magia.")
                return objeto.regenerar_magia()
            print("Lich usa ataque basico.")
            return objeto.ataque_basico(enemigo)

    class IA_ArchiMago:
        def __init__(self):
            pass
        def evalua_situacion_magia(self, objeto, enemigo):
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
                print("Error en IA Archimago: " + str(e))
                return 0
    class IA_General:
        def __init__(self):
            pass
        def evaluar(self, objeto, enemigo, aliados=None):
            energia = objeto.get_energia()
            if energia >= 1000 and objeto.get_cooldown() == 0:
                dado = random.randint(1, 4)
                if dado==1:
                    objeto.canion_especial_final(enemigo)
                elif dado == 2:
                    objeto.tiro_doble(enemigo)
                elif dado == 3:
                    objeto.carga_de_caballeria(enemigo)
                elif dado ==4:
                    objeto.espada(enemigo)
            elif energia<1000 and objeto.get_cooldown() ==0:
                    dado = random.randint(1, 3)
                    if dado == 1:
                        objeto.tiro_doble(enemigo)
                    elif dado == 2:
                        objeto.carga_de_caballeria(enemigo)
                    elif dado ==3:
                        objeto.espada(enemigo)
                    else:
                        print('Error')

    class IA_Clerigo:
        def __init__(self):
            pass
        def evaluar(self, objeto, enemigo, aliados):
            mas_herido = None
            menor_vida = 9999
            for aliado in aliados:
                if aliado.get_visible() and aliado.get_vida() < aliado.get_vida_max() * 0.5:
                    if aliado.get_vida() < menor_vida:
                        menor_vida = aliado.get_vida()
                        mas_herido = aliado
            if mas_herido is not None and objeto.get_magia() >= 200 and objeto.get_cooldown() == 0:
                print("Clerigo cura a aliado herido.")
                return objeto.sanacion_grupal(mas_herido)
            elif objeto.get_magia() >= 100 and objeto.get_cooldown() == 0:
                print("Clerigo usa palabras de fe contra enemigo.")
                return objeto.palabras_de_fe(enemigo)
            else:
                print("Clerigo usa ataque basico.")
                return objeto.ataque_basico(enemigo)

    class IA_Guerrero:
        def __init__(self):
            pass
        def evaluar(self, objeto, enemigo):
            if objeto.get_vida() < objeto.get_vida_max() * 0.3:
                print("Guerrero usa testudo para defenderse.")
                return objeto.testudo()
            elif random.random() < 0.2:
                print("Guerrero usa arremeter.")
                return objeto.arremeter()
            else:
                print("Guerrero ataca.")
                return objeto.ataque_basico(enemigo)

    class IA_Arquero:
        def __init__(self):
            pass        
        def evaluar(self, objeto, enemigo):
            if objeto.get_carcaj() <= 1 and objeto.get_flecha_trucada()<=1:
                print("Arquero sin flechas. Recarga.")
                return objeto.recarga_rapida()
            dado = random.randint(1, 10)
            if dado == 1 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero dispara flecha normal.")
                return objeto.disparar_flechas(enemigo)
            elif dado == 2 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa flecha de hielo.")
                return objeto.flecha_de_hielo(enemigo)
            elif dado == 3 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa flecha venenosa.")
                return objeto.flecha_venenosa(enemigo)
            elif dado == 4 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa tiro doble.")
                return objeto.tiro_doble(enemigo)
            elif dado == 5 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa flecha electrica")
                return objeto.flecha_electrica
            elif dado == 6 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa explosiva")
                return objeto.flecha_explosiva
            elif dado == 7 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa flecha sombria")
                return objeto.flecha_sombria
            elif dado == 8 and objeto.get_carcaj()>0 and objeto.get_flecha_trucada() >= 1:
                print("Arquero usa flecha especial")
                return objeto.flechita_especial
            else:
                print("Arquero dispara flecha normal.")
                return objeto.disparar_flechas(enemigo)
    class IA_Dragon:
        def __init__(self):
            pass
        def evaluar(self, objeto, enemigo):
            magia = objeto.get_magia()
            if objeto.get_escamas_activas() == 0 and magia >= 30:
                print("Dragon activa escamas reflectantes.")
                return objeto.escamas_reflectantes()
            if magia >= 200:
                dado = random.randint(1, 10)
                if dado <= 4:
                    print("Dragon usa llamarada infernal.")
                    return objeto.ataque_llamarada_infernal(enemigo)
                elif dado <= 6:
                    print("Dragon usa ataque de espinas.")
                    return objeto.ataque_espinas(enemigo)
                elif dado <= 8 and magia >= 100:
                    print("Dragon usa rayo de luz.")
                    return objeto.ataque_luz(enemigo)
                else:
                    print("Dragon usa ataque basico.")
                    return objeto.ataque_basico(enemigo)
            else:
                print("Dragon usa ataque basico.")
                return objeto.ataque_basico(enemigo)
