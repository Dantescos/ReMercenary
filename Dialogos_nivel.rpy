# ============================================================
# DIALOGOS DE LOS NIVELES - RE: MERCENARY
# ============================================================

define kazuki = Character("Kazuki", color="#88ccff")
define lyra = Character("Lyra", color="#ff88cc")
define gromm = Character("Gromm", color="#008000")
define senor_oscuro = Character("Senor Oscuro", color="#8B0000")

# ============================================================
# NIVEL 1
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
    gromm  "Podria ser un hechicero poderoso el que los controla o un nigromante."
    kazuki "Entonces tenemos que detenerlos antes de que sea tarde."
    gromm  "Juntos podremos acabar contra esos goblins y salvar la aldea."
    lyra   "¿Estan seguros? Podrian morir."
    kazuki "Morir ya lo hice una vez. No me asusta."
    gromm  "Niña, estoy tan seguro como que los seguiria hasta el infierno mismo."
    lyra   "..."
    kazuki "Vamos. Tengo un plan para salvar la aldea."
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel1_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "Los goblins yacen derrotados. La aldea esta a salvo."
    lyra    "Lo logramos. Pero fue demasiado facil."
    kazuki  "¿Facil? Casi me mata el orco."
    gromm   "Si, esto es extraño."
    lyra    "Me refiero a que no deberia haber sido tan facil. Los goblins no tienen esa fuerza."
    kazuki  "Entonces hay algo mas grande detras."
    gromm   "Se los dije, seguro es algun hechicero o algun brujo."
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
# NIVEL 2
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
    lyra   "Esto es diferente. Los muertos estan organizados. Como un ejercito."
    gromm  "Entonces hay alguien detras. Alguien con un plan."
    kazuki "Vamos. Averiguemos quien es."
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
    "La Cripta esta en silencio. Los muertos vuelven a descansar."
    kazuki "Encontre esto entre los restos del Dragon."
    "Kazuki sostiene un medallon con el simbolo del Imperio Oscuro."
    lyra   "Es la marca del General Oscuro. El segundo al mando."
    kazuki "Entonces el esta detras de la reanimacion."
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
# NIVEL 3
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
    lyra   "Cuidado. En este bosque, los arboles tambien atacan."
    gromm  "Que ataquen. Yo les respondo con mi hacha."
    lyra   "Gromm, no todo se resuelve con violencia."
    gromm  "En mi experiencia, casi todo si."
    hide kazuki
    hide lyra
    hide gromm
    return

label dialogo_nivel3_victoria:
    scene black
    show kazuki at left
    show lyra at right
    show gromm at center
    "El Ogro Berserker cae. El bosque recupera un poco de su color."
    lyra   "El Ogro tenia esto."
    "Lyra sostiene un mapa de Veridia con marcas rojas."
    kazuki "¿Que son estas marcas?"
    lyra   "Ubicaciones del Imperio. El General esta reuniendo su ejercito en el Templo de los Caidos."
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
# NIVEL 4
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
    kazuki "Activen los interruptores. Con eso abriremos el camino al General."
    lyra   "¿Y si no los encontramos todos?"
    kazuki "Entonces no saldremos. Y esto habra sido en vano."
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
    "El Caballero Caido se desmorona. Su armadura negra cae al suelo."
    kazuki "Pobre hombre. Fue corrompido por el Imperio."
    lyra   "Era el capitan de la guardia real segun las notas que encontre."
    kazuki "¿Y como termino asi convertido en un ser corrompido?"
    lyra   "El General lo traiciono. Le prometio poder y lo convirtio en un monstruo."
    gromm  "Conocia a ese hombre. Era un buen soldado. Un buen lider."
    kazuki "Gromm..."
    gromm  "El General pagara por esto. Lo juro por mi barba."
    lyra   "Entonces el General no es solo un enemigo. Es un traidor."
    kazuki "Por eso tenemos que detenerlo. No solo por Veridia. Por todos los que cayeron."
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 5
# ============================================================
label dialogo_nivel5_inicio:
    scene black
    "La Fortaleza del General se alza sobre una colina, rodeada de un foso de fuego."
    "Es el corazon del ejercito enemigo."
    show kazuki at left
    show lyra at right
    show gromm at center
    gromm  "Esta es la fortaleza mas grande que he visto."
    lyra   "El General debe estar en el centro. Con sus tropas de elite."
    kazuki "Entonces iremos directo al centro. Sin escalas."
    gromm  "Me gusta como piensas, muchacho. Siempre directo al grano."
    lyra   "Pero tengan cuidado. El General invoca esqueletos."
    kazuki "Entonces lo matamos antes de que invoque demasiados. Es simple."
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
    "El General Oscuro cae. Su capa roja se mancha de sangre."
    kazuki "Se acabo. El ejercito del Imperio esta en retirada."
    lyra   "Por ahora. Pero el Senor Oscuro sigue vivo."
    kazuki "Lo se. Y mientras viva, la guerra no terminara."
    gromm  "Entonces vamos por el. Directo al Abismo."
    lyra   "Espera. El Abismo no es un lugar comun. Es una caverna infernal."
    kazuki "¿Y eso que importa?"
    lyra   "Que si entramos, tal vez no salgamos."
    gromm  "Entonces saldremos por la puerta que hagamos con nuestras espadas."
    kazuki "Eso no tiene sentido, Gromm."
    gromm  "Lo se. Pero suena bien, ¿no?"
    lyra   "..."
    kazuki "Vamos. Al Abismo."
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 6
# ============================================================
label dialogo_nivel6_inicio:
    scene black
    "El Abismo de los Condenados es una caverna al pie del volcan."
    "Se dice que el Senor Oscuro usa este lugar para sus rituales."
    show kazuki at left
    show lyra at right
    show gromm at center
    gromm  "Huele a azufre. Y a muerte."
    lyra   "Este es el lugar. El Senor Oscuro esta aqui."
    kazuki "Recuerden el plan. Gromm, aguanta los ataques. Lyra, dispara desde lejos."
    lyra   "¿Eso es tu plan? ¿'Ver que haces'?"
    kazuki "Soy estratega, no heroe. Los planes se hacen sobre la marcha."
    gromm  "¡Me parece bien, golpeare tanto a ese señor oscuro que no quedara nada de el!"
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
    "El Senor Oscuro cae de rodillas. Pero no esta muerto."
    "Se levanta. Su cuerpo se retuerce."
    show senor_oscuro at center
    senor_oscuro "¿Crees que puedes matarme? ¡Soy eterno!"
    kazuki "Nadie es eterno. Ni tu."
    senor_oscuro "Calla, humano insolente! Has arruinado mis planes pero aun tengo mas sorpresas!"
    gromm "Ah si? Pues demuestra todo lo que tienes, estupido fanfarron!"
    senor_oscuro "¡Entonces mira mi verdadero poder, humano insolente!"
    hide senor_oscuro
    "El Senor Oscuro se transforma. Su piel se vuelve escamas. Sus ojos, fuego."
    "La Fase 2 ha comenzado."
    show kazuki at left
    show lyra at right
    show gromm at center
    lyra   "¡Kazuki! ¡Tenemos que ir al Trono!"
    kazuki "¡Vamos! ¡Esto no termina aca!"
    gromm  "¡Que alguien me explique que acaba de pasar!"
    kazuki "¡Despues, Gromm! ¡Corran!"
    hide kazuki
    hide lyra
    hide gromm
    return

# ============================================================
# NIVEL 7
# ============================================================
label dialogo_nivel7_inicio:
    scene black
    "La Sala del Trono. El corazon del Imperio Oscuro."
    "El Senor Oscuro esta sentado en su trono, esperando."
    show senor_oscuro at center
    senor_oscuro "Los esperaba. Tardaron mas de lo que pense."
    show kazuki at left
    show lyra at right
    show gromm at center
    kazuki "La paciencia no es tu fuerte, ¿verdad?"
    senor_oscuro "La paciencia es para los debiles. Yo soy un dios."
    gromm  "¡No eres un dios! ¡Eres un tirano! ¡Y los tiranos caen!"
    senor_oscuro "Entonces vengan. Muestrenme su fuerza."
    lyra   "Esto es tu final, tirano."
    gromm  "¡Por Veridia! ¡Por los caidos! ¡Y por mi familia!"
    senor_oscuro "Patetico. Pero admiro su valentia. Los mataremos de forma lenta para disfrutar de sus gritos de agonia, malditos insectos!"
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
    "El Senor Oscuro cae. Su trono se desmorona. El Imperio, tambien."
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
    "Kazuki y Lyra se toman de las manos oficializando su relacion amorosa. Gromm mira al paisaje dejando a los dos tortolos."
    "FIN"
    return