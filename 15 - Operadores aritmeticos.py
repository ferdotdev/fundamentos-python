"""
Para realizar operaciones aritméticas en Python, necesitamos dos valores, que pueden 
ser numeros enteros, flotantes o variables que contengan estos valores.
"""

a = 10
b = 3

# Suma
print(a + b)

# Resta
print(a - b)

# Multiplicación
print(a * b)

# División
print(a / b)

# División entera
print(a // b)

# Módulo
print(a % b)

# Potenciación
print(a ** b)

"""
El orden de las operaciones aritméticas en Python sigue las reglas de PEMDAS 

Paréntesis
Exponentes
Multiplicación
División
Adición
Sustracción

Esto significa que las 
operaciones dentro de paréntesis se realizan primero, seguidas por exponentes, luego
multiplicación y división y finalmente adición y sustracción (ambas leídas de izquierda a derecha).
"""

print((a + b) * (a - b) / b)

"""
Podemos usar operadores aritméticos para crear funciones que realicen cálculos específicos.
Por ejemplo, podemos crear una función para verificar si un número es impar o par.
"""

def is_odd(number):
    return number % 2 != 0

print(is_odd(4)) 

def is_even(number):
    return number % 2 == 0

print(is_even(2)) 