# ============================================================
# DIALOGOS DE LOS NIVELES - RE: MERCENARY
# ============================================================

define kazuki = Character("Kazuki", color="#88ccff")
define lyra = Character("Lyra", color="#ff88cc")
define gromm = Character("Gromm", color="#008000")
define senor_oscuro = Character("Senor Oscuro", color="#8B0000")
define traidor = Character("Traidor", color="#FF6600")

# ============================================================
# NIVEL 1: LA INVASION DE LOS GOBLINS (Boss: Ogro)
# ============================================================
label dialogo_nivel1_inicio:
    scene black
    "Hace tres dias, los goblins atacaron y masacraron a los aldeanos de la aldea de Piedra Blanca."
    "Nadie sabe de donde vinieron. Pero nadie duda de que hay algo detras."

    show kazuki at left
    show lyra at right
    show gromm at center
    kazuki "Esto es una masacre. Los goblins no suelen atacar de esta forma."
    lyra   "No son solo goblins. Hay esqueletos. Y algo mas."
    gromm  "Por lo visto no solo se han vuelto mas agresivos, sino que mas organizados."
    kazuki "¿Que quieres decir, Lyra?"
    lyra   "Que alguien los esta controlando. Y quien los controle, tiene un plan."
    gromm  "Podria ser un hechicero poderoso o un nigromante."
    kazuki "Entonces tenemos que detenerlos antes de que sea tarde."
    gromm  "Juntos podremos acabar con esos goblins y salvar la aldea."
    lyra   "¿Estan seguros? Podrian morir."
    kazuki "Morir ya lo hice una vez. No me asusta."
    gromm  "Niña, estoy tan seguro como que los seguiria hasta el infierno mismo."
    lyra   "..."
    kazuki "Vamos. Un Ogro lidera a los goblins. Si lo matamos, la horda se dispersa."
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel1_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "El Ogro cae con un golpe seco. Los goblins restantes huyen despavoridos."
    lyra    "Lo logramos. Pero fue demasiado facil."
    kazuki  "¿Facil? Casi me mata el ogro ese."
    gromm   "Si, esto es extraño."
    lyra    "Me refiero a que no deberia haber sido tan facil. Los goblins no tienen esa fuerza."
    kazuki  "Entonces hay algo mas grande detras."
    gromm   "Se los dije, seguro es algun hechicero."
    lyra    "El Imperio Oscuro. Tiene que ser ellos."
    kazuki  "Si es asi, esto recien empieza."
    gromm   "¿Y como estas tan segura, elfa?"
    lyra    "Tengo un mal presentimiento."
    kazuki  "Si es asi, debemos prepararnos para lo peor."
    gromm   "Ojala te equivoques, elfa."
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 2: LA CRIPTA OLVIDADA (Boss: Esqueleto)
# ============================================================
label dialogo_nivel2_inicio:
    scene black
    "Tras salvar la aldea, el trio se dirige a la Cripta Olvidada."
    "Un cementerio antiguo donde descansan los heroes olvidados por el tiempo."
    show kazuki at left
    show lyra at right
    show gromm at center
    gromm  "Este lugar me da escalofrios. Los muertos no deberian caminar."
    lyra   "Por eso estamos aca. Alguien los esta despertando."
    kazuki "¿Tu crees que sea un nigromante?"
    lyra   "O algo peor. Un nigromante solo reanima cadaveres. Pero esto..."
    lyra   "Los muertos estan organizados. Como un ejercito."
    gromm  "Entonces hay alguien detras. Alguien con un plan."
    kazuki "Vamos. El Esqueleto nigromante debe estar en el centro de la cripta."
    gromm  "Y si nos encontramos con el, le cortare la cabeza con mi hacha."
    lyra   "Siempre tan sutil, enano."
    gromm  "Es lo que mejor se me da, niña."
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel2_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "El Esqueleto nigromante se desmorona. Su craneo rueda por el suelo."
    kazuki "Encontre esto entre sus ropas."
    "Kazuki sostiene un medallon con el simbolo del Imperio Oscuro."
    lyra   "Es la marca del Imperio. Alguien de alto rango esta detras."
    kazuki "Entonces esto es mas grande de lo que pensabamos."
    gromm  "Un general necesita un ejercito. Y que mejor que los muertos."
    lyra   "Tiene sentido. Pero hay algo que no me cierra."
    kazuki "¿Que cosa?"
    lyra   "¿Por que el Imperio estaria reanimando muertos en un lugar tan sagrado?"
    gromm  "Para burlarse de los caidos. Los del Imperio son unos hijos de..."
    kazuki "Gromm."
    gromm  "... Perdon."
    lyra   "Descansemos. Manana iremos al Bosque de las Sombras."
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 3: EL BOSQUE DE LAS SOMBRAS (Boss: Traidor)
# ============================================================
label dialogo_nivel3_inicio:
    scene black
    "El Bosque de las Sombras era un lugar sagrado para los elfos."
    "Ahora, sus arboles estan negros y sus ramas se retuercen como garras."
    show kazuki at left
    show lyra at right
    show gromm at center
    lyra   "Este bosque... era mi hogar. Antes de que el Imperio lo quemara."
    kazuki "Lo siento, Lyra."
    lyra   "No es tu culpa. Pero encontrar esto asi... es como perderlo dos veces."
    gromm  "Los arboles estan vivos, pero no de la forma correcta. Algo los corrompio."
    kazuki "El mismo algo que reanima a los muertos. Tenemos que seguir avanzando."
    lyra   "Cuidado. Hay alguien aqui. Siento su presencia."
    gromm  "Que ataque. Yo les respondo con mi hacha."
    "Una figura encapuchada aparece entre las sombras."
    traidor "Los estaba esperando. Que bueno que vinieron a morir."
    kazuki "¡Tu! ¡Eres el Traidor que vendio al rey!"
    traidor "Traicion es una palabra fea. Yo lo llamo... supervivencia."
    gromm  "¡Vas a morir por lo que hiciste!"
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel3_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "El Traidor cae de rodillas. Su mascara se rompe."
    traidor "Miserables... el Senor Oscuro... no perdonara esto..."
    kazuki "El Senor Oscuro vendra por nosotros, ya lo sabemos."
    traidor "Viene... viene por todo Veridia. Y ustedes... no podran detenerlo..."
    "El Traidor exhala su ultimo aliento."
    lyra   "El Traidor tenia esto."
    "Lyra sostiene un mapa de Veridia con marcas rojas."
    kazuki "¿Que son estas marcas?"
    lyra   "Ubicaciones del Imperio. El Senor Oscuro esta reuniendo su ejercito en el Templo de los Caidos."
    kazuki "Entonces iremos alli."
    gromm  "Ya era hora de pelear contra algo mas grande."
    lyra   "Espera. Hay algo mas. Esta marca... esta justo en mi aldea."
    kazuki "Lyra..."
    lyra   "No. No es momento para sentimentalismos. Vamos al Templo. Ya."
    gromm  "Niña, si necesitas hablar de eso..."
    lyra   "No. No necesito."
    kazuki "Vamos, entonces."
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 4: EL TEMPLO DE LOS CAIDOS (Boss: Caballero Corrompido)
# ============================================================
label dialogo_nivel4_inicio:
    scene black
    "El Templo de los Caidos fue construido para honrar a los heroes del reino."
    "Ahora, sus pasillos estan llenos de trampas y sus salas, de espectros."
    show kazuki at left
    show lyra at right
    show gromm at center
    gromm  "Conozco este lugar. Luche aqui cuando era joven."
    kazuki "¿En serio?"
    gromm  "Si. Fue mi primera batalla como soldado. Perdimos contra el Imperio."
    lyra   "Esta vez sera diferente."
    gromm  "Eso espero. Porque si perdemos, Veridia cae."
    kazuki "El Caballero Corrompido custodia el templo. Fue un heroe, ahora es un monstruo."
    lyra   "¿Puede ser salvado?"
    kazuki "No lo se. Pero si esta corrompido, no nos quedara otra opcion."
    gromm  "Sin presion, ¿eh?"
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel4_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "El Caballero Corrompido se desmorona. Su armadura negra cae al suelo."
    "Debajo, hay un hombre viejo. Su rostro es familiar."
    gromm  "¡Por todos los dioses! ¡Es el Capitan Aldric!"
    kazuki "¿Lo conoces?"
    gromm  "Era el capitan de la guardia real. Un buen hombre. Un buen lider."
    lyra   "El Imperio lo corrompio. Le prometio poder y lo convirtio en un monstruo."
    kazuki "Pobre hombre. Fue traicionado por los que servia."
    gromm  "El Senor Oscuro pagara por esto. Lo juro por mi barba."
    lyra   "Entonces el Senor Oscuro no es solo un enemigo. Es un monstruo que corrompe a los heroes."
    kazuki "Por eso tenemos que detenerlo. No solo por Veridia. Por todos los que cayeron."
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 5: LA FORTALEZA DEL GENERAL (Boss: Senor Oscuro Humano)
# ============================================================
label dialogo_nivel5_inicio:
    scene black
    "La Fortaleza del Imperio se alza sobre una colina, rodeada de un foso de fuego."
    "Es el corazon del ejercito enemigo."
    show kazuki at left
    show lyra at right
    show gromm at center
    gromm  "Esta es la fortaleza mas grande que he visto."
    lyra   "El Senor Oscuro debe estar en el centro. Con sus tropas de elite."
    kazuki "Entonces iremos directo al centro. Sin escalas."
    gromm  "Me gusta como piensas, muchacho. Siempre directo al grano."
    lyra   "Pero tengan cuidado. El Senor Oscuro es poderoso. Dicen que puede transformarse."
    kazuki "Entonces lo matamos antes de que lo haga. Es simple."
    gromm  "Simple dice. Nada es simple cuando hay magia de por medio."
    kazuki "Por eso tenemos a Lyra. Para que sea simple."
    lyra   "Pero mi magia es distinta."
    gromm  "Explicate, elfa."
    lyra   "Puedo manipular elementos naturales solo un poco."
    gromm  "¿Un poco? ¿A que te refieres?"
    lyra   "Es que... no soy un Alto Elfo."
    gromm  "Pero eres mas alta que yo, de que patrañas hablas."
    kazuki "Lo que ella quiere decir es que no puede usar magia porque no es Alto Elfo."
    gromm  "Ohhh... eso explica porque no usas magia."
    kazuki "No te preocupes Lyra, aun asi con o sin magia eres una elfa poderosa."
    gromm  "Si, tienes una excelente punteria, elfa."
    lyra   "Gracias a los dos."
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel5_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    show senor_oscuro at center
    "El Senor Oscuro, en su forma humana, cae de rodillas. Su capa roja se mancha de sangre."
    senor_oscuro "Impresionante... nadie habia llegado tan lejos..."
    kazuki "Se acabo. El Imperio esta en retirada."
    senor_oscuro "¿Crees que esto es el final? Patetico."
    "El Senor Oscuro se levanta. Su cuerpo se retuerce."
    senor_oscuro "¡Entonces mira mi VERDADERO poder, humano insolente!"
    hide senor_oscuro
    "El Senor Oscuro se transforma. Su piel se vuelve escamas. Sus ojos, fuego."
    "Sus alas se despliegan. Ya no es un hombre. Es un demonio."
    "La Fase 2 ha comenzado."
    show kazuki at left
    show lyra at right
    show gromm at center
    lyra   "¡Kazuki! ¡Tenemos que ir al Abismo!"
    kazuki "¡Vamos! ¡Esto no termina aca!"
    gromm  "¡Que alguien me explique que acaba de pasar!"
    kazuki "¡Despues, Gromm! ¡Corran!"
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 6: EL ABISMO DE LOS CONDENADOS (Boss: Senor Oscuro Demonio)
# ============================================================
label dialogo_nivel6_inicio:
    scene black
    "El Abismo de los Condenados es una caverna al pie del volcan."
    "El Senor Oscuro ha huido aqui. En su forma demoniaca, es aun mas peligroso."
    show kazuki at left
    show lyra at right
    show gromm at center
    gromm  "Huele a azufre. Y a muerte."
    lyra   "Este es el lugar. El Senor Oscuro esta aqui."
    kazuki "Recuerden el plan. Gromm, aguanta los ataques. Lyra, dispara desde lejos."
    lyra   "¿Eso es tu plan? ¿'Ver que haces'?"
    kazuki "Soy estratega, no heroe. Los planes se hacen sobre la marcha."
    gromm  "¡Me parece bien, golpeare tanto a ese demonio que no quedara nada de el!"
    lyra   "Ustedes dos me van a volver loca."
    kazuki "Entonces al menos moriremos con estilo."
    lyra   "..."
    kazuki "Era un chiste, Lyra."
    lyra   "No tiene gracia."
    gromm  "A mi me hizo gracia."
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel6_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    show senor_oscuro at center
    "El Señor Oscuro (demonio) cae. Sus alas se quiebran. Pero no esta muerto."
    senor_oscuro "¿Crees que puedes matarme? ¡Soy eterno!"
    kazuki "Nadie es eterno. Ni tu."
    senor_oscuro "Calla, humano insolente! Has arruinado mis planes pero aun tengo mas sorpresas!"
    gromm "Ah si? Pues demuestra todo lo que tienes, estupido fanfarron!"
    senor_oscuro "¡Entonces mira mi VERDADERA forma, humano insolente!"
    hide senor_oscuro
    "El Demonio se retuerce. Sus alas se desgarran. Su carne se deshace."
    "De su cuerpo emergen tentaculos. Su forma ya no es humanoide."
    "La Fase 3 ha comenzado. EL SEÑOR OSCURO REVELA SU FORMA FINAL."
    show kazuki at left
    show lyra at right
    show gromm at center
    lyra   "¡Kazuki! ¡Esto no es un demonio! ¡Es algo peor!"
    kazuki "¡Vamos al Trono! ¡Es nuestra ultima oportunidad!"
    gromm  "¡Que alguien me explique que acaba de pasar!"
    kazuki "¡Despues, Gromm! ¡Corran!"
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 7: EL TRONO DEL SENOR OSCURO (Boss: Senor Oscuro Tentaculos)
# ============================================================
label dialogo_nivel7_inicio:
    scene black
    "La Sala del Trono. El corazon del Imperio Oscuro."
    "En el trono, algo que ya no puede llamarse humano espera."
    show senor_oscuro at center
    senor_oscuro "Los esperaba... aunque ya no puedo verlos con ojos humanos..."
    show kazuki at left
    show lyra at right
    show gromm at center
    kazuki "¿Que te has hecho a ti mismo?"
    senor_oscuro "Me he convertido... en lo que siempre fui... en la PODREDUMBRE misma."
    gromm  "¡No eres un dios! ¡Eres un monstruo! ¡Y los monstruos caen!"
    senor_oscuro "Entonces vengan. Muestrenme su fuerza... si es que aun tienen alguna."
    lyra   "Esto es tu final, tirano."
    gromm  "¡Por Veridia! ¡Por los caidos! ¡Y por mi familia!"
    senor_oscuro "Patetico. Pero admiro su valentia. Los devorare... lentamente."
    kazuki "Eso lo veremos."
    hide kazuki
    hide lyra
    hide gromm
    hide senor_oscuro
    return

label dialogo_nivel7_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "El Monstruo de Tentaculos se desmorona. Su cuerpo vuelve a su forma humana."
    "El Senor Oscuro, ahora un anciano debil, yace en el suelo."
    senor_oscuro "Lo lograron... al fin... alguien pudo detenerme..."
    kazuki "¿Por que? ¿Por que hiciste todo esto?"
    senor_oscuro "Porque... tenia miedo. Miedo de morir. Miedo de perder... todo."
    senor_oscuro "El poder... me consumio. Pero ustedes... ustedes no se rindieron."
    "El Senor Oscuro exhala su ultimo aliento. El Imperio Oscuro ha caido."
    "Pero no hay tiempo para celebrar. Veridia esta en ruinas."
    kazuki "Lo logramos. Pero... ¿a que costo?"
    lyra   "Veridia sobrevivira. Los reinos siempre lo hacen."
    kazuki "¿Y nosotros?"
    lyra   "¿Nosotros? Depende de ti, Kazuki."
    gromm  "Niña, dejalo respirar. Acaba de salvar el mundo."
    lyra   "Solo digo que..."
    kazuki "Lo se. Lo se."
    "Lyra lo mira con una sonrisa."
    lyra   "¿Te vas a quedar, Kazuki? ¿O vas a volver a tu mundo?"
    kazuki "..."
    kazuki "Me quedare."
    "Kazuki y Lyra se toman de las manos. Gromm mira al paisaje."
    "FIN"
    return