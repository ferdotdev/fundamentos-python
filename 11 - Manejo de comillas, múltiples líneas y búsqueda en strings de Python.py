# Comillas multiples en Python

# Comillas dentro de comillas
print("Hola 'mundo'")
print('Hola "mundo"')

# Múltiples líneas con comillas triples
multiples = """Hola
Mundo"""
print(multiples)

# in y not in - Búsqueda en strings

texto = "Este curso es de fundamentos de Python"
print("Python" in texto)   # True
print("python" in texto)   # False (por *case sensitive*)
print("JavaScript" not in texto)  # True

#.upper y .lower - Convierte a mayúsculas y minúsculas

mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula) # MAYUSCULA
print(minuscula) # minuscula

#.strip - Elimina espacios al inicio y al final
espacios = "   este es el texto   "
sin_espacios = espacios.strip()
print(sin_espacios)