"""
Desempaquetado en Python

El desempaquetado es una característica de Python que permite asignar los 
elementos de cualquier iterable a variables individuales de manera sencilla.

Estos iterables pueden ser listas, tuplas, strings, rangos, sets y diccionarios.
"""
tup = (1, 2, 3)

x, y, z = tup

print(x)  # Salida: 1
print(y)  # Salida: 2
print(z)  # Salida: 3

"""
Importante debe haber el mismo numero de variables que elementos en el iterable,
de lo contrario se producirá un error.
"""
tupla = (1, 2)
# x, y, z = tupla  # ValueError: not enough values to unpack

lista = [1, 2, 3, 4]
# x, y, z = lista  # ValueError: too many values to unpack

"""
Desempaquetado extendido
"""

lista = [1, 2, 3, 4, 5]
primero, *medio, ultimo = lista # El * captura múltiples elementos
print(primero)  # 1
print(medio)    # [2, 3, 4]
print(ultimo)   # 5

"""
Aqui Python asigna en orden:

Primero asigna las variables SIN asterisco (de izquierda a derecha)
El asterisco captura "todo lo que sobre" o hasta que encuentra otra variable sin asterisco
y lo asigna a la variable con asterisco, en este caso "medio"

Finalmente asigna la variable sin asterisco al final, en este caso "ultimo"

En el desempaquetado extendido, solo una variable puede tener el asterisco
y esta puede estar en cualquier posición.
"""

"""
Multiplicación de listas y tuplas
"""

# Multiplicación de tuplas

tech_companies = ("Google", "Apple", "Microsoft")
print(tech_companies * 2)

"""
Suma de listas y tuplas

Tambien se pueden sumar listas y tuplas, lo que resulta en una nueva lista o tupla
que contiene los elementos de ambas.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)