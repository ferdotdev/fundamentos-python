# Booleanos en Python

# La forma de escribir booleanos en Python es con la primera letra en mayuscula
T = True
F = False

# Las comparaciones devuelven booleanos
print(3 == 3) # True
print(5 > 3) # True
print(5 > 10) # False

# Castear a booleano
print(bool("Hi")) # Cualquier string no vacio se convierte a True
print(bool(1)) # Cualquier numero distinto de 0 se convierte a True
print(bool(["manzana", "pera"])) # Cualquier lista no vacia se convierte a True

# Casos que se convierten a False

print(bool("")) # Cualquier string vacio se convierte a False
print(bool(0)) # El numero 0 se convierte a False
print(bool([])) # Las listas vacias se convierten a False
print(bool(None)) # None se convierte a False

# Verificacion de tipos con isinstance

x = 0
y = 1
z = True

print(isinstance(x, int)) # Si el valor coincide con el tipo de dato = True
print(isinstance(y, bool)) # 1 No se convierte a True con isinstance = False