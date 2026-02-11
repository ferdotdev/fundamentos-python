"""
Tuplas

Son colecciones ordenadas e inmutables. 
Se definen utilizando paréntesis () y los elementos se separan por comas.

También pueden contener elementos duplicados al igual que las listas.
"""

tech_companies = ('Google', 'Apple', 'Y Combinator', 'Meta', 'Amazon', 'NVIDIA')
print(tech_companies)


# Las tuplas tambien usan indices para acceder a sus elementos
# al igual que las listas, diccionarios y strings, se usan los
# corchetes el operador de indice 

print(tech_companies[2])

# Podemos usar len() para saber la longitud de una tupla
print(len(tech_companies))

"""
Una tupla puede contener diferentes tipos de datos, como enteros, strings, 
decimales, booleanos, listas, sets y diccionarios, pero no pueden ser modificados 
después de su creación.
"""

mixed_tuple = (1, "hola", 3.14, True, [1, 2, 3], {1, 2, 3}, {'clave': 'valor'})
print(mixed_tuple)
print(type(mixed_tuple))

"""
Recorrer tuplas
"""

for item in mi_tupla:
    print('Tupla recorrida:', item)


"""
En las tuplas, al ser inmutables, no podemos usar muchos de los metodos que usamos
en las listas, como append(), extend(), insert(), pop(), remove() y clear().

La unica forma de modificar una tupla es convirtiendola a una lista, modificando 
la lista y luego convirtiendola de nuevo a una tupla.
"""