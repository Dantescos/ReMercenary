# ============================================================
# DIALOGOS DE LOS NIVELES - RE: MERCENARY
# ============================================================

# ============================================================
# NIVEL 1: LA INVASION DE LOS GOBLINS
# ============================================================

label dialogo_nivel1_inicio:
    scene black
    "Hace tres dias, los goblins atacaron la aldea de Piedra Blanca."
    "Nadie sabe de donde vinieron. Pero nadie duda de que hay algo detras."
    
    show kazuki at left
    show lyra at right
    
    kazuki "Esto es una masacre. Los goblins no suelen atacar de esta forma."
    lyra "No son solo goblins. Hay esqueletos. Y algo mas."
    kazuki "¿Que quieres decir?"
    lyra "Que alguien los esta controlando. Y quien los controle, tiene un plan."
    kazuki "Entonces tenemos que detenerlos antes de que sea tarde."
    lyra "¿Estas seguro? Podrias morir."
    kazuki "Morir ya lo hice una vez. No me asusta."
    lyra "..."
    kazuki "Vamos. La aldea no se va a salvar sola."
    
    hide kazuki
    hide lyra
    
    return

label dialogo_nivel1_victoria:
    scene black
    show kazuki at left
    show lyra at right
    
    "Los goblins yacen derrotados. La aldea esta a salvo."
    
    lyra "Lo logramos. Pero fue demasiado facil."
    kazuki "¿Facil? Casi me mata el orco."
    lyra "Me refiero a que no deberia haber sido tan facil. Los goblins no tienen esa fuerza."
    kazuki "Entonces hay algo mas grande detras."
    lyra "El Imperio Oscuro. Tiene que ser ellos."
    kazuki "Si es asi, esto recien empieza."
    lyra "Descansemos. Manana tendremos que ir a la fortaleza enemiga."
    kazuki "De acuerdo. Pero primero, revisemos si hay sobrevivientes."
    
    hide kazuki
    hide lyra
    
    return