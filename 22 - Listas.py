"""
Listas

Las listas en Python son colecciones ordenadas, que permiten mutabilidad, ademas que permiten
contener elementos duplicados y de diferentes tipos de datos.
"""

tesla_models = ['Model S', 'Model 3', 'Model X', 'Model Y', 'CyberTruck']

print(tesla_models)

# Para acceder a un elemento de la lista se utiliza el indice
print(tesla_models[4])

# Las listas son mutables, lo que significa que se pueden modificar después de su creación.
tesla_models[0] = 'S'
tesla_models[1] =  3
tesla_models[2] = 'X'
tesla_models[3] = 'Y'

print('Tesla is', tesla_models)

# Las listas pueden contener elementos de diferentes tipos de datos
mixed_list = ['Tesla', 'Model', 3, True]

# Para saber la longitud de una lista se utiliza la función len()
print(len(mixed_list))

# Rangos de indices en una lista

# En Python los rangos no incluyen el valor final, por lo que `1:3` imprime los elementos del 1 al 2.
print(tesla_models[1:3])

# Imprime desde el inicio hasta el indice 2 (Indice 3 no incluido)
print(tesla_models[:3])

# Imprime desde el indice 1 hasta el final
print(tesla_models[1:])

# Saber si un elemento esta en la lista

# Mediante una condicional if se puede verificar si un elemento esta presente 
# en la lista utilizando el operador `in`.

if 'X' in tesla_models:
    print('Model X available!')

tesla_models.pop(4)


# Rellenar una lista con for

lista = []

for i in range(1,6):
    lista.append(i)

print(lista)

# Metodos

frutas = ['manzana', 'banana', 'naranja']

# Append - Agregar un elemento al final de la lista

frutas.append('pera')
print(frutas)

# Insert - Permite insertar en la posicion deseada, no elimina el elemento que se encuentra 
# en esa posicion, sino que lo desplaza una posicion a la derecha. 
# El primer parametro es el indice y el segundo el elemento a insertar

frutas.insert(1, 'uva')
print(frutas)

# Remove - Elimina el elemento declarado, si existe

frutas.remove('manzana')
print(frutas)

# Pop - Permite eliminar el elemento declarando el indice

frutas.pop(3)
print(frutas)

# Sort - Para ordenar alfabeticamente, de menor a mayor, o de mayor a menor dependiendo 
# del tipo de datos que contenga la lista.

frutas.sort()
print(frutas)

# Reverse - Para ordenar a la inversa

frutas.reverse()
print(frutas)

# Unir listas

new_list = tesla_models + frutas
print(new_list)
