dia = 'lun'

match dia:
    case 'lun':
        print("Hoy es Lunes")
    case 'mar':
        print("Hoy es Martes")
    case 'mié':
        print("Hoy es Miércoles")
    case 'jue':
        print("Hoy es Jueves")
    case 'vie':
        print("Hoy es Viernes")
    case 'sáb':
        print("Hoy es Sábado")
    case 'dom':
        print("Hoy es Domingo")
    case _: # Caso por defecto
        print("Día no válido")