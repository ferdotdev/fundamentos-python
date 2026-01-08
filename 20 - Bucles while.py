"""
Bucles While
Como su nombre lo indica, los bucles while se ejecutan mientras 
una condicion sea verdadera
"""

i = 1

while i <= 10:
    print(i)
    i += 1 # Sin el mas 1 de incremento, el bucle sería infinito

"""
Break

Break sirve para salir de un bucle si se cumple una condicion
en este caso, una condicion if

La condicion break es afectada unicamente si el dato de la condicion es exacto
Si el incrementador fuera 2, se saltaria el valor
Saltandose la condicion de break tambien
"""

j = 1
while j <= 10:
    if j == 5:
        break
    print(j)
    j += 1

"""
Continue
"""

k = 0

while k < 10:
    k += 1 
    if k == 5:
        continue
    print(k)
else:
    print("El bucle ha finalizado correctamente")