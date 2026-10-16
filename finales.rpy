# ============================================================
# RE: MERCENARY - FINALES DEL JUEGO (CON MÚSICA POR FINAL)
# ============================================================

# ============================================================
# FINAL BUENO
# ============================================================
label final_bueno:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_bueno.wav", fadein=1.5, loop=True)
    $ desbloquear_logro("final_bueno")
    scene negro with fade
    "La ultima batalla ha llegado a su fin. Las fuerzas de la oscuridad se desvanecen en el horizonte y el silencio regresa a las tierras de Veridia."
    "Kazuki, Lyra y Gromm se mantienen en pie, firmes tras la victoria."
    "En el pueblo, la celebracion no tarda en comenzar, aunque los ancianos y lugareños murmuran con cautela en las tabernas..."
    "Se dice que, a pesar de la caida de la señora oscura, algunos de sus secuaces mas fieles aun siguen sus ordenes ocultos en las sombras, esperando el momento propicio."
    "Pero eso ya no importa hoy. Kazuki decide quedarse junto a Lyra y Gromm, listos y preparados para embarcarse en muchas mas aventuras juntos."
    "¡HAS COMPLETADO EL JUEGO - FINAL BUENO!"
    call screen creditos_animados
    $ detener_musica(fadeout=1.0)
    jump menu_principal

# ============================================================
# FINAL MALO
# ============================================================
label final_malo:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_malo.wav", fadein=1.5, loop=True)
    $ desbloquear_logro("final_malo")
    scene negro with fade
    "El poder del señor oscuro era abrumador. La ultima linea de defensa colapso en cuestion de segundos."
    "Kazuki usa un hechizo de magia oscura que no lograba dominar para pelear contra la señora oscura, pero falla,
    cae de rodillas sobre la tierra fria, viendo como todo por lo que lucho se desvanece."
    "La señora oscuro gana la contienda definitiva, arrasando con todo a su paso y matando a todos los que se interponen en su camino."
    "La oscuridad eterna se cierne sobre el mundo, sellando un destino sin esperanza."
    "GAME OVER - FINAL MALO"
    $ detener_musica(fadeout=1.0)
    jump menu_principal

# ============================================================
# FINAL AGRIDULCE (OVERLORD)
# ============================================================
label final_agridulce:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_agridulce.wav", fadein=1.5, loop=True)
    $ desbloquear_logro("final_overlord")
    scene negro with fade
    "La victoria se sintio distinta esta vez. Al reclamar el poder absoluto del enemigo vencido, algo dentro de Kazuki cambio para siempre."
    "Kazuki: todo este poder, puedo gobernar el mundo...Ser lo que no pude ser en la vida real"
    "La ambicion y la oscuridad del artefacto corrompieron su mente de forma irreversible."
    "Ya no hay vuelta atras. Kazuki se corrompe por completo por el poder y gobierna con mano de hierro, volviendose un tirano implacable sobre las tierras que juro proteger."
    "GAME OVER - FINAL OVERLORD"
    $ detener_musica(fadeout=1.0)
    jump menu_principal

# ============================================================
# FINAL ISEKAI I (regresa al hospital, sin daño)
# ============================================================
label final_isekai_1:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_isekai_I.wav", fadein=1.5, loop=True)
    $ desbloquear_logro("final_isekai")
    scene negro with fade
    "Un destello cegador lo consumio todo. El ruido de la batalla se transformo de golpe en el molesto pitido constante de unos monitores."
    "Kazuki abre lentamente los ojos y ve las paredes blancas de una habitacion de hospital."
    "Sobre su mesa de luz, descansando pacificamente, se encuentra el pendiente de Lyra, brillando con una luz tenue."
    "Una sensacion extraña lo invade, dejandolo con la duda perpetua de si todo fue solo un sueño... o si realmente ocurrio."
    "Kazuki: todo esto...fue...real?"
    "FIN - FINAL ISEKAI I"
    $ detener_musica(fadeout=1.0)
    jump menu_principal

# ============================================================
# FINAL ISEKAI II (regresa al hospital, piernas cortadas)
# ============================================================
label final_isekai_2:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_isekai_II.wav", fadein=1.5, loop=True)
    $ desbloquear_logro("final_isekai")
    scene negro with fade
    "El impacto final lo expulso de aquel mundo de fantasia de la manera mas cruel."
    "Kazuki despierta de golpe en la fria cama de un hospital, sintiendo un vacio extraño y pesado en la parte baja de su cuerpo."
    "Al mirar hacia abajo, descubre con horror que despierta en el hospital con las piernas cortadas, consecuencia del brutal accidente que lo arrastro al coma."
    "La aventura termino de la forma mas dolorosa en el mundo real."
    "Kazuki: NOOOOOOOOOOOOOOOOOOOOO!!!!! MIS PIERNAAAAAAAAAAS!"
    "FIN - FINAL ISEKAI II"
    $ detener_musica(fadeout=1.0)
    jump menu_principal

# ============================================================
# FINAL SACRIFICIO
# ============================================================
label final_sacrificio:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_sacrificio.wav", fadein=1.5, loop=True)
    $ desbloquear_logro("final_bueno")
    scene negro with fade
    "Sin pensarlo un solo segundo, Kazuki se abalanza y se interpone en la trayectoria del ataque."
    "Kazuki recibe el ultimo ataque final de la señora oscuro y cae herido de muerte, protegiendo a su compañera."
    "El silencio inunda el campo de batalla. Lyra se arrodilla junto a el y lo abraza llorando desconsoladamente."
    "Kazuki: Lyra...."
    "Lyra: Kazuki no hables, por favor no te esfuerces"
    "Kazuki: Siento...no habertelo dicho antes...Siempre me gustastes...."
    "Gromm: por favor niño, guarda tus fuerzas...Lyra usa tu magia de sanacion o algo!"
    "Lyra: No sirve! No sirve!"
    "Kazuki: Esta bien...no...pas...pasa..nada...Tu magia no sirve...porque la magia con la que me hirieron es...mas...fuerte"
    "Lyra: Nooo..Kazuki,lo siento , por favor...Yo...yo...yo"
    "Kazuki: Tranquila....gracias....a..los dos....soy tan feliz de haberlos conocidos..."
    "Kazuki cierra los ojos lentamente con una sonrisa y muere en los brazos de Lyra, Lyra lo abraza mas fuerte mientras llora."
    "Gromm aprieta los puños, con lagrimas en los ojos pero mirando hacia otro lado, conteniendo su dolor."
    "Con el sacrificio de Kazuki, la amenaza es contenida y todo vuelve a la paz en el reino, aunque el precio pagado fue la vida de Kazuki."
    "FIN - FINAL DEL SACRIFICIO"
    call screen creditos_animados
    $ detener_musica(fadeout=1.0)
    jump menu_principal


# ============================================================
# ELECCIÓN FINAL CONTRA LA SEÑORA OSCURA
# ============================================================
label eleccion_ataque_final_boss:
    "¡El señor oscura desata su poder maximo! Un rayo letal se dirige directamente hacia Lyra."
    
    menu:
        "¿Que accion deseas tomar?"
        "ESQUIVAR":
            jump final_bueno
        "SALVAR A LYRA":
            jump final_sacrificio
        "MATAR A LA SEÑORA OSCURA":
            jump final_agridulce
        "USAR MAGIA OSCURA Y LANZAR HECHIZO A SEÑORA OSCURA":
            jump final_malo