"""
Listas

Las listas en Python son colecciones ordenadas, que permiten mutabilidad, ademas que permiten
contener elementos duplicados y de diferentes tipos de datos.
"""

tesla_models = ['Model S', 'Model 3', 'Model X', 'Model Y', 'CyberTruck']

print(tesla_models)
print(tesla_models[4])

tesla_models[0] = 'S'
tesla_models[1] =  3
tesla_models[2] = 'X'
tesla_models[3] = 'Y'

tesla_models.pop(4)

print('Tesla is', tesla_models)
print(len(tesla_models))

# Nota: En Python los rangos no incluyen el valor final, por lo que `1:3` imprime los elementos del 1 al 2.
print(tesla_models[1:3])

# Imprime desde el inicio hasta el indice 2 (3  no incluido)
print(tesla_models[:3])

# Imprime desde el indice 1 hasta el final
print(tesla_models[1:])


# Rellenar una lista con for

lista = []

for i in range(1,6):
    lista.append(i)

print(lista)

if 'X' in tesla_models:
    print('Model X available!')

# Metodos

# Append - Al final de la lista

# Insert - Permite insertar en la posicion deseada

# Remove - Permite eliminar el elemento declarado, si existe

# Pop - Permite eliminar el elemento declarando el indice

# Sort - Para ordenar

# Reverse - Para ordenar a la inversa

# Unir listas

new_list = old_list + other_old_list
print(new_list)
