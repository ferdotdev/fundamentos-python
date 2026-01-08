"""
Operadores de asignacion
En Python, los operadores de asignación se utilizan para asignar valores a las variables.
"""

x = 100    # Asignacion de valores simple
x = x + 3  # Asignacion de variables simple

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
y = 5
y //= 2    # Operador de asignacion de division entera
y **= 3    # Operador de asignacion de potencia

"""
Operador walrus

Es el operador de asignación de expresión (también conocido como
el "operador walrus" :=), que permite asignar valores a las variables como parte
de una expresión.
"""

print(y := 2) 
