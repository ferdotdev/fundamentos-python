"""
Condicionales if, else, and, or y pass

En este ejemplo, se muestran diferentes estructuras condicionales, combinadas
con el uso de operadores logicos, para controlar la ejecucion del codigo.

if es la primera condicion que se evalua. Si es verdadera, se ejecuta el codigo
Si es falsa, se pasa a la siguiente o siguientes condiciones elif (else if) 
Si ninguna de las condiciones if o elif es verdadera, se ejecuta el codigo dentro del bloque else.

Ademas, se utiliza la palabra reservada 'pass' para indicar que no se realiza
ninguna accion en un bloque condicional.
"""

a = 10
b = 5
c = 10

if a < b and a == c:
    print("a es menor que b y a es igual a c")
elif a < b or b < c: 
    print("Al menos una de las condiciones es verdadera")
else:
    print("Condicion no cumplida")

if not(a == b):
    pass