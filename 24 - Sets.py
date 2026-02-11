"""
Sets (Conjuntos) en Python

Los sets son colecciones no ordenadas, se definen utilizando llaves {} 
o la función set(), estos son mutables y no permiten elementos duplicados.

Si existen elementos duplicados no arrojan un error, simplemente se ignoran 
y no se agregan al set.
"""

frutas = {'manzana', 'banana', 'naranja', 'manzana'}
print(frutas)

# La longitud del set es 3, ya que 'manzana' se repite y se ignora 
print(len(frutas)) 

"""
Un set puede contener diferentes tipos de datos INMUTABLES (hashables), 
como enteros, strings, decimales, booleanos, tuplas (con elementos hashables) 
y frozensets, además, puede ser modificado después de su creación.

No pueden contener listas, diccionarios u otros sets, ya que estos NO son 
hashables (mutables o no tienen hash definido).
"""

mixed_set = {1, "hola", 3.14, True}
print(mixed_set)
print(type(mixed_set))