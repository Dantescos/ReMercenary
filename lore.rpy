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
# Kazuki Tanaka tenia 28 anos, vivia solo, y su unico logro en la vida
# era ser el numero 1 en el ranking global de "Kingdom Tactics",
# un juego de estrategia por turnos que nadie jugaba fuera de Japon.
#
# Una noche, despues de derrotar al jefe final por la centesima vez,
# salio a comprar ramen. Un camion lo atropello.
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
#   empieza a confiar en el.
#
# - Gromm: Caballero enano, leal hasta la muerte. Fue soldado del
#   ejercito real antes de la invasion. Su familia murio en el
#   primer ataque del Imperio Oscuro.
#
# - Morgana: Maga misteriosa. Nadie sabe de donde viene. Ella sabe
#   que Kazuki es un isekai, pero no lo revela. Tiene sus propios
#   motivos para luchar.

# ============================================================
# EL ANTAGONISTA: EL SENOR OSCURO
# ============================================================
# No es malvado. Es un idealista. Quiere unificar el mundo bajo su
# imperio para acabar con las guerras. Pero esta dispuesto a matar
# a cualquiera que se interponga en su camino.
#
# En otra vida, pudo haber sido un gran rey. En esta, es un tirano.

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