# ============================================================
# RE: MERCENARY - FINALES DEL JUEGO
# ============================================================
# FINAL BUENO
# ============================================================
label final_bueno:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_bueno.wav", fadein=1.5, loop=True)
    $ registrar_final_visto("final_bueno")  
    $ desbloquear_logro("final_bueno")


    scene final_bueno_veridia with fade
    "La ultima batalla ha llegado a su fin. Las fuerzas de la oscuridad se desvanecen en el horizonte y el silencio regresa a las tierras de Veridia."
    "Kazuki, Lyra y Gromm se mantienen en pie, firmes tras la victoria, contemplando el amanecer sobre las ruinas."

    scene final_bueno_goblins with dissolve
    "En el pueblo, la celebracion no tarda en comenzar, aunque los ancianos y lugareños murmuran con cautela en las tabernas..."
    "Se dice que, a pesar de la caida de la Señora Oscura, algunos de sus secuaces mas fieles aun siguen sus ordenes ocultos en las sombras, esperando el momento propicio."
    "Los goblins siguen atacando aldeas lejanas. La guerra no termino del todo. ¡ESTO ES SOLO EL COMIENZO!"

    scene final_bueno_diario with dissolve
    "Pero eso ya no importa hoy. Kazuki decide quedarse junto a Lyra y Gromm, listos y preparados para embarcarse en muchas mas aventuras juntos."
    "Sentado en un acantilado, anota en su diario cada una de las historias que aun estan por venir."

    kazuki "Bitacora, dia 33. Comenzare diciendo que nuestros esfuerzos han dado frutos. Hemos podido neutralizar a mas de los secuaces mas leales de la Señora Oscura. Yo habia creido que esto habria terminado."
    kazuki "Cuan equivocado estaba. Esto apenas comienza."
    kazuki "..."
    kazuki "Segun los aventureros de la taberna, me ha llegado la informacion de dos grupos que le eran leales a la Señora Oscura."
    kazuki "Se hacen llamar LOS DIEZ INFIERNOS, sus subditos mas fieles, y LOS SIN ROSTROS, un culto de fanaticos a la Señora Oscura que mata sin dejar pistas y se desconoce sus intenciones."
    kazuki "Segun los reportes de los aldeanos, los Sin Rostros nunca dejan testigos, y los Diez Infiernos responden directamente a la voluntad de su señora muerta."
    kazuki "Tsk... Dos grupos problematicos..."
    kazuki "Lo bueno es que no estoy solo en esto. Gromm, mi mejor amigo, y mi novia Lyra, seguimos luchando por la paz."
    kazuki "Ademas, estamos yendo a las tabernas para reclutar a mas heroes. Necesitamos toda la ayuda posible."
    kazuki "..."
    kazuki "Seguire peleando hasta mi ultimo aliento. No voy a dejar que las fuerzas del mal ganen."
    kazuki "Por Veridia. Por Lyra. Y por mi."
    "Fin de bitacora."
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
    $ registrar_final_visto("final_malo")   # <-- CAMBIO
    $ desbloquear_logro("final_malo")

    scene final_malo_derrota with fade
    "El poder de la Señora Oscura era abrumador. La ultima linea de defensa colapso en cuestion de segundos."
    "Kazuki cae de rodillas sobre la tierra fria, viendo como todo por lo que lucho se desvanece."
    "Lyra y Gromm, derrotados a su lado. La Señora Oscura se alza victoriosa sobre ellos."

    scene final_malo_veridia with dissolve
    "La Señora Oscura gana la contienda definitiva, arrasando con todo a su paso y matando a todos los que se interponen en su camino."
    "Desde lo alto de la torre, contempla Veridia arder. Los demonios invaden cada calle, cada casa, cada sueño."
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
    $ registrar_final_visto("final_agridulce")  
    $ desbloquear_logro("final_agridulce")

    scene final_agridulce_trono with fade
    "La victoria se sintio distinta esta vez. Al reclamar el poder absoluto del enemigo vencido, algo dentro de Kazuki cambio para siempre."
    kazuki "Todo este poder... puedo gobernar el mundo... Ser lo que nunca pude ser en la vida real."
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
    $ registrar_final_visto("final_isekai_1") 
    $ desbloquear_logro("final_isekai_1")

    scene isekai1_manos with fade
    "Un destello cegador lo consumio todo. El ruido de la batalla se transformo de golpe en el molesto pitido constante de unos monitores."
    "Kazuki abre lentamente los ojos. Se mira las manos. Sin heridas. Sin magia. Solo piel."

    scene isekai1_habitacion with dissolve
    "Paredes blancas. Luz de hospital. Sabanas limpias. El techo de una habitacion que reconoce, pero que ya no siente como suya."

    scene isekai1_pendiente with dissolve
    "Sobre su mesa de luz, descansando pacificamente, se encuentra el pendiente de Lyra, brillando con una luz tenue."
    "Una sensacion extraña lo invade, dejandolo con la duda perpetua de si todo fue solo un sueño... o si realmente ocurrio."
    "FIN - FINAL ISEKAI I"

    $ detener_musica(fadeout=1.0)
    jump menu_principal


# ============================================================
# FINAL ISEKAI II (regresa al hospital, piernas amputadas)
# ============================================================
label final_isekai_2:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_isekai_II.wav", fadein=1.5, loop=True)
    $ registrar_final_visto("final_isekai_2") 
    $ desbloquear_logro("final_isekai_2")

    scene isekai2_manos with fade
    "Un destello cegador lo consumio todo. El ruido de la batalla se transformo de golpe en el molesto pitido constante de unos monitores."
    "Kazuki abre los ojos. Se mira las manos. Y por un instante, cree que todo fue un sueño."

    scene isekai2_habitacion with dissolve
    "Pero el frio de la habitacion lo golpea. La lluvia golpea la ventana. El silencio pesa demasiado."

    scene isekai2_piernas with dissolve
    "Al mirar hacia abajo, descubre con horror que despierta en el hospital con las piernas cortadas, consecuencia del brutal accidente que lo arrastro al coma."
    "La aventura termino de la forma mas dolorosa en el mundo real."
    "FIN - FINAL ISEKAI II"

    $ detener_musica(fadeout=1.0)
    jump menu_principal


# ============================================================
# FINAL SACRIFICIO
# ============================================================
label final_sacrificio:
    $ detener_musica(fadeout=1.0)
    $ reproducir_musica("final_sacrificio.wav", fadein=1.5, loop=True)
    $ registrar_final_visto("final_sacrificio") 
    $ desbloquear_logro("final_sacrificio")

    scene final_sacrificio_rayo with fade
    "Sin pensarlo un solo segundo, Kazuki se abalanza y se interpone en la trayectoria del ataque."
    "Kazuki recibe el ultimo ataque de la Señora Oscura, protegiendo a su compañera. Pero con sus ultimas fuerzas, lanza su hechizo mas poderoso."

    kazuki "¡No te dejare ganar! Yo... protegere Veridia... y... mis amigos..."

    scene final_sacrificio_contraataque with dissolve
    kazuki "¡TOMA ESTO! ¡VOLLZANBEL!"
    "Kazuki lanza su hechizo mas poderoso contra la Señora Oscura, poniendole fin a su tirania."

    scene final_sacrificio_kazuki with dissolve
    kazuki "Lyra..."
    lyra "Kazuki, no hables. Por favor, no te esfuerces."
    kazuki "Siento... no habertelo dicho antes... Siempre me haz gustado..."
    gromm "¡Por favor niño, guarda tus fuerzas... Lyra, usa tu magia de sanacion o algo!"
    lyra "¡No sirve! ¡No sirve!"
    kazuki "Esta bien... no... pasa... nada... Tu magia no sirve... porque la magia con la que me hirieron es... mas... fuerte..."
    lyra "Nooo... Kazuki... lo siento... por favor... yo... yo... yo..."
    kazuki "Tranquila... gracias... a los dos... soy tan feliz de haberlos conocido... Gracias por esta aventura."

    scene final_sacrificio_abrazo with dissolve
    "Kazuki cierra los ojos lentamente con una sonrisa y muere en los brazos de Lyra. Lyra lo abraza mas fuerte mientras llora."
    "Gromm aprieta los puños, con lagrimas en los ojos pero mirando hacia otro lado, conteniendo su dolor."
    "Con el sacrificio de Kazuki, la amenaza es contenida y todo vuelve a la paz en el reino, aunque el precio pagado fue la vida de un heroe."

    call screen creditos_animados
    $ detener_musica(fadeout=1.0)
    jump menu_principal


# ============================================================
# ELECCION FINAL CONTRA LA SEÑORA OSCURA
# ============================================================
label eleccion_ataque_final_boss:
    "¡La Señora Oscura desata su poder maximo! Un rayo letal se dirige directamente hacia Lyra."

    menu:
        "¿Que accion deseas tomar?"
        "USAR MAXIMO PODER Y SALVAR A LYRA":
            jump final_bueno
        "USAR CUERPO COMO ESCUDO":
            jump final_sacrificio
        "MATAR A LA SEÑORA OSCURA CON MAGIA OSCURA":
            jump final_agridulce
        "IGNORAR Y LANZAR HECHIZO A SEÑORA OSCURA":
            jump final_malo