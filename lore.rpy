# ============================================================
# LORE DE RE: MERCENARY
# ============================================================

# ============================================================
# EL MUNDO: EL REINO DE VERIDIA
# ============================================================
# Veridia era un reino prospero, famoso por sus tierras fertiles
# y sus caballeros honorables. Pero todo cambio cuando el
# Imperio Oscuro comenzo su invasion.
#
# Los generales legitimos murieron en batalla. El rey, desesperado,
# ofrece una recompensa a cualquier mercenario que pueda detener
# el avance enemigo.
#
# Nadie sospecha que el hombre que comandara la resistencia no es
# de este mundo.

# ============================================================
# EL PROTAGONISTA: KAZUKI TANAKA
# ============================================================
# Kazuki Tanaka es un fracasado profesional. Tiene 28 años, vive solo, y su único logro 
# en la vida es ser el número 1 en el ranking global de "Kingdom Tactics", un juego de 
# estrategia por turnos que nadie juega fuera de Japón.
#
# Una noche, después de derrotar al jefe final por la centésima vez, sale a comprar ramen.
# Un camion lo atropella. Cuando despierta, esta en un mundo de fantasia medieval.
# Pero no es un heroe elegido por una diosa. No tiene habilidades sobrehumanas. 
# Desperto en el cuerpo de Sir Alaric, un comandante mercenario arruinado, alcohólico y endeudado. 
# Su ejercito: tres soldados veteranos y un caballo cojo. Su reputación: tan mala que los campesinos le escupen al pasar.

# El reino de Veridia esta en guerra contra el Imperio Oscuro. Los generales legitimos han muerto. 
# El rey ofrece una recompensa a cualquier mercenario que pueda detener el avance enemigo. Kazuki no quiere ser héroe.
# Quiere volver a casa. Pero para sobrevivir necesita oro. Y para ganar oro necesita ganar batallas. 
# Por suerte, tiene algo que nadie más tiene: 3000 horas de experiencia en Kingdom Tactics.
#
# Una noche, despues de derrotar al jefe final por la centesima vez,salio a comprar ramen. Un camion lo atropello.
#
# Cuando desperto, estaba en un mundo de fantasia medieval.
# Pero no era un heroe elegido por una diosa. No tenia habilidades
# sobrehumanas. Desperto en el cuerpo de Sir Alaric, un comandante
# mercenario arruinado, alcoholico y endeudado.

# ============================================================
# LOS COMPANEROS
# ============================================================
# Kazuki no esta solo. Tiene tres aliados:
#
# - Lyra: Arquera elfa, la mejor del reino. Fue rescatada por Kazuki
#   de un ataque goblin. Desconfia de los humanos, pero poco a poco
#   empieza a confiar en el y enamorarse de el.
#
# - Gromm: Caballero enano, leal hasta la muerte. Fue soldado del
#   ejercito real antes de la invasion. Su familia murio en el
#   primer ataque del Imperio Oscuro. El juro vengarse del señor Oscuro
#   y su ejercito
#
# - Morgana: Maga misteriosa. Nadie sabe de donde viene. Ella sabe
#   que Kazuki es un humano fuera de este mundo, pero no lo revela. 
#    Tiene sus propios motivos para luchar.
#
# ============================================================
# EL ANTAGONISTA: EL SENOR OSCURO
# ============================================================
# No es malvado. Es un idealista. Quiere unificar el mundo bajo su
# imperio para acabar con las guerras. Pero esta dispuesto a matar
# a cualquiera que se interponga en su camino.
#
# En otra vida, pudo haber sido un gran rey. En esta, es un tirano.
# Y esta decidido a realizar sus metas incluso si tiene que matar a Kazuki
# y sus amigos.

# ============================================================
# SCREEN DE LORE (para mostrar en el menu)
# ============================================================
screen pantalla_lore():
    modal True
    frame:
        xfill True
        yfill True
        background "#0a0a1a"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text "LORE DE VERIDIA" size 50 color "#ffcc00" bold True xalign 0.5
            
            text "El reino de Veridia era un paraiso." size 22 color "#ffffff" xalign 0.5
            text "Hasta que el Imperio Oscuro llego." size 22 color "#ffffff" xalign 0.5
            text "Ahora, un mercenario de otro mundo" size 22 color "#88ccff" xalign 0.5
            text "debe salvarlo... o morir en el intento." size 22 color "#88ccff" xalign 0.5
            
            textbutton "Cerrar":
                action Return()
                text_size 25
                xalign 0.5