#Automatización del DFD-Bandersnatch.

    
# Función para contar la primera parte de la historia
def historia_inicio():
    print("Stefan, un joven programador, está creando un videojuego.")
    print("Tiene una reunión importante con una empresa de videojuegos.")
    decisión = input("¿Quieres que Stefan vaya a la reunión? (si/no): ").lower()

    if decisión == "si":
        reunion_si()
    elif decisión == "no":
        reunion_no()
    else:
        print("Opción no válida, intenta de nuevo.")
        historia_inicio()

#Elige ir a la reunión
def reunion_si():
    print("Stefan va a la reunión y se encuentra con un importante productor.")
    decisión = input("¿Acepta trabajar con ellos? (si/no): ").lower()

    if decisión == "si":
        final_exito()
    elif decisión == "no":
        print("Stefan rechaza la oferta y sigue trabajando solo.")
        decisión = input("¿Continúa solo en el proyecto? (si/no): ").lower()

        if decisión == "si":
            final_aislamiento()
        else:
            final_fracaso()
    else:
        print("Opción no válida, intenta de nuevo.")
        reunion_si()

#Decide no ir a la reunión
def reunion_no():
    print("Stefan decide no ir a la reunión y sigue trabajando solo.")
    decisión = input("¿Sigue trabajando en el proyecto solo? (si/no): ").lower()

    if decisión == "si":
        decisión = input("¿Empieza a sospechar que lo están controlando? (si/no): ").lower()

        if decisión == "si":
            final_paranoico()
        else:
            final_aislamiento()
    else:
        final_fracaso()

# Finales posibles
def final_exito():
    print("Stefan trabaja con la empresa y el juego se convierte en un éxito.")
    print("¡Has llegado al final exitoso!")

def final_rechazo():
    print("Stefan rechaza la oferta de la empresa.")
    print("Desafortunadamente, el juego no logra ser exitoso. Final triste.")

def final_aislamiento():
    print("Stefan se aísla trabajando solo en su proyecto.")
    print("El proyecto lo consume y pierde el control sobre su vida. Final oscuro.")

def final_fracaso():
    print("Stefan abandona el proyecto y cae en la desesperación.")
    print("Nunca logra finalizar el juego. Final trágico.")

def final_paranoico():
    print("Stefan empieza a sospechar que alguien lo está controlando.")
    print("Pierde el sentido de la realidad y confronta a 'su controlador'.")
    decisión = input("¿Quiere descubrir quién lo controla? (sí/no): ").lower()

    if decisión == "sí":
        final_cuarta_pared()
    else:
        final_psiquiatrico()

def final_cuarta_pared():
    print("Stefan se da cuenta de que está dentro de una historia controlada por alguien.")
    print("Rompe la cuarta pared y descubre que sus decisiones no son suyas. Final surrealista.")

def final_psiquiatrico():
    print("Stefan pierde el control por completo y es internado en un psiquiatra.")
    print("El juego nunca es terminado. Final psiquiátrico.")

# Llamada inicial
historia_inicio()