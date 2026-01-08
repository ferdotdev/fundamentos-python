# Operadores de comparacion

"""
Estos operadores nos permiten comparar valores y devolver un valor booleano (True o False)
los cuales nos indican si la comparacion es verdadera o falsa.
"""

x = 5
y = 3

# Igual a
print(x == y)

# Diferente de
print(x != y) 

# Mayor que
print(x > y)

# Menor que
print(x < y)   

# Mayor o igual que
print(x >= y)

# Menor o igual que
print(x <= y)

# Operadores logicos and, or y not

"""
Estos operadores logicos nos permiten combinar multiples condiciones booleanas
y devolver un valor booleano (True o False) basado en la evaluacion de esas condiciones
"""

# AND: Verdadero si ambas condiciones son verdaderas
print(x > 2 and y < 5)

# OR: Verdadero si alguna de las condiciones es verdadera
print(x > 2 or y > 5)

# NOT: Invierte el valor booleano de la condicion
print(not(x > 2))