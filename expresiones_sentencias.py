""" Expresiones y Sentencias

Expresiones (expressions):
Son cualquier cosa que produce o que tiene un valor.
Algo que se puede “evaluar” y da un resultado.

Ejemplos de expresiones:
1 + 2 # Operación aritmética
"hola".upper() # Llamada a método
x # Variable
x > 10 # Comparación
len([1, 2, 3]) # Llamada a función
z := 3 # Asignación con operador walrus (Python 3.8+)

Si lo puedes asignar o usar dentro de un print probablemente es una expresión.

Sentencias (statements):

Una sentencia es una instrucción completa que Python ejecuta, pero no es un valor en sí misma.
Es decir son las órdenes que le das al intérprete: "Haz algo con este dato"

Si es parte de la estructura del programa, es una sentencia.

Ejemplos de sentencias:

# Asignación de variable

x = 3

# Funciones

def foo():
    return 123

# Clases

class MiClase:
    pass

# Sentencias de control
if x > 10:
    print("grande")

# Ciclo

for i in range(5):
print(i)

# Try/Except

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero.")

# Importaciones

import math

No puedes guardar una sentencia dentro de una expresion, pero puedes guardar una expresión dentro de una sentencia.

print(x = 3) # SyntaxError
print(1 + 2) # Resultado: 3
print(z := 2) # Resultado: 2
"""