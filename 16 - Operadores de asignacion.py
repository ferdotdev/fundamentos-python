"""
Operadores de asignacion
En Python, los operadores de asignación se utilizan para asignar valores a las variables.
"""

x = 100    # Asignacion inicial
x = x + 3  # Asignacion simple
x += 3     # Asignacion con operador de suma
x -= 2     # Asignacion con operador de resta
x *= 4     # Asignacion con operador de multiplicacion
x /= 2     # Asignacion con operador de division
x %= 3     # Asignacion con operador de modulo

y = 5
y //= 2    # Asignacion con operador de division entera
y **= 3    # Asignacion con operador de potencia

"""
Operador walrus

Es el operador de asignación de expresión (también conocido como
el "operador walrus" :=), que permite asignar valores a las variables como parte
de una expresión.
"""
print(y := 2) 
