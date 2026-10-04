screen pantalla_lore():
    modal True
    tag menu

    on "show" action Play("music", "audio/lore.wav", fadein=1.0, loop=True)

    add Solid("#0a0a1a")

    text "LORE DE VERIDIA":
        xalign 0.5
        ypos 20
        size 45
        color "#ffcc00"
        bold True

    text "EL MUNDO: EL REINO DE VERIDIA\n\nVeridia era un reino próspero, famoso por sus tierras fértiles y sus caballeros honorables. Pero todo cambió cuando el Imperio Oscuro comenzó su invasión.\n\nLos generales legítimos murieron en batalla. El rey, desesperado, ofrece una recompensa a cualquier mercenario que pueda detener el avance enemigo.\n\nNadie sospecha que el hombre que comandará la resistencia no es de este mundo.\n\nEL PROTAGONISTA: KAZUKI TANAKA\n\nKazuki Tanaka es un fracasado profesional. Tiene 28 años, vive solo, y su único logro en la vida es ser el número 1 en el ranking global de Kingdom Tactics, un juego de estrategia por turnos que nadie juega fuera de Japón.\n\nUna noche, después de derrotar al jefe final por la centésima vez, sale a comprar ramen. Un camión lo atropella. Cuando despierta, está en un mundo de fantasía medieval. Pero no es un héroe elegido por una diosa. No tiene habilidades sobrehumanas. Despertó en el cuerpo de Sir Alaric, un comandante mercenario arruinado, alcohólico y endeudado. Su ejército: tres soldados veteranos y un caballo cojo. Su reputación: tan mala que los campesinos le escupen al pasar.\n\nEl reino de Veridia está en guerra contra el Imperio Oscuro. Los generales legítimos han muerto. El rey ofrece una recompensa a cualquier mercenario que pueda detener el avance enemigo. Kazuki no quiere ser héroe. Quiere volver a casa. Pero para sobrevivir necesita oro. Y para ganar oro necesita ganar batallas. Por suerte, tiene algo que nadie más tiene: 3000 horas de experiencia en Kingdom Tactics.\n\nLOS COMPAÑEROS\n\nKazuki no está solo. Tiene tres aliados:\n\nLyra: Arquera elfa, la mejor del reino. Fue rescatada por Kazuki de un ataque goblin. Desconfía de los humanos, pero poco a poco empieza a confiar en él y enamorarse de él.\n\nGromm: Caballero enano, leal hasta la muerte. Fue soldado del ejército real antes de la invasión. Su familia murió en el primer ataque del Imperio Oscuro. Él juró vengarse del Señor Oscuro y su ejército.\n\nMorgana: Maga misteriosa. Nadie sabe de dónde viene. Ella sabe que Kazuki es un humano fuera de este mundo, pero no lo revela. Tiene sus propios motivos para luchar.\n\nEL ANTAGONISTA: EL SEÑOR OSCURO\n\nNo es malvado. Es un idealista. Quiere unificar el mundo bajo su imperio para acabar con las guerras. Pero está dispuesto a matar a cualquiera que se interponga en su camino.\n\nEn otra vida, pudo haber sido un gran rey. En esta, es un tirano. Y está decidido a realizar sus metas incluso si tiene que matar a Kazuki y sus amigos.":
        xalign 0.5
        ypos 90
        xsize 1800
        text_align 0.5
        size 20
        color "#ffffff"
        line_spacing 4

    textbutton "Cerrar":
        xalign 0.5
        yalign 0.97
        text_size 25
        action [Stop("music", fadeout=0.5), Play("music", "audio/inicio.wav", fadein=1.0, loop=True), ShowMenu("main_menu")]