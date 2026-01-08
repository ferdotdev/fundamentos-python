"""
Operadores de asignacion
En Python, los operadores de asignación se utilizan para asignar valores a las variables.
"""

x = 100    # Asignacion de valores simple
x = x + 3  # Reasignacion de variables

"""
Operadores de asignacion

Los operadores de asignación pueden usarse con numeros o con otras variables
"""
x += z     # Operador de asignacion con otra variable
x += 3     # Operador de asignacion de suma
x -= 2     # Operador de asignacion de resta
x *= 4     # Operador de asignacion de multiplicacion
x /= 2     # Operador de asignacion de division
x %= 3     # Operador de asignacion de modulo
x //= 2    # Operador de asignacion de division entera
x **= 3    # Operador de asignacion de potencia

"""
Este operador realizara la operacion y asignara el resultado a la variable
"""

"""
Operador walrus

Representado con := 

Este es el operador de asignación de expresión, también conocido como
el operador walrus, que permite asignar valores a las variables como parte
de una expresión.
"""

print(y := 2) 
