"""
Match

La estructura match-case en Python permite evaluar una variable
y ejecutar diferentes bloques de código según el valor de esa variable.
Es similar a la estructura switch-case en otros lenguajes de programación.
"""

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