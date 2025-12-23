dia = 'po'

match dia:
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miércoles")
    case 4:
        print("Hoy es Jueves")
    case 5:
        print("Hoy es Viernes")
    case 6:
        print("Hoy es Sábado")
    case 7:
        print("Hoy es Domingo")
    case _: # Caso por defecto
        print("Día no válido")