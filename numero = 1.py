numero = 5
match numero:
    case 1: 
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case 1:
        print("Uno")
    case _: # default
        print("Número no reconocido")