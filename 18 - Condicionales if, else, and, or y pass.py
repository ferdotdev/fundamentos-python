"""
Condicionales if, else, and, or y pass

Las estructuras condicionales, combinadas
con el uso de operadores logicos, nos ayudan a controlar la ejecucion del codigo

if, else y elif

if es la primera condicion que se evalua

Si es verdadera, se ejecuta el codigo
Si es falsa, se pasa a la siguiente o siguientes condiciones elif (else if) 
Si ninguna de las condiciones if o elif es verdadera, se ejecuta el codigo 
dentro del bloque else.
"""

if a < b:
    print("a es menor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es mayor que b")

"""
Condicionales con operadores logicos

Los operadores logicos and, or y not nos permiten combinar multiples condiciones
booleanas dentro de una estructura condicional
"""

if a < b and a == c:
    print("a es menor que b y a es igual a c")
elif a < b or b < c: 
    print("Al menos una de las condiciones es verdadera")
else:
    print("Condicion no cumplida")

if not (a > b):
    print("a no es mayor que b")


"""
Ademas, se utiliza la palabra reservada 'pass' para indicar que no se realiza
ninguna accion en un bloque condicional.
"""

if not(a == b):
    pass