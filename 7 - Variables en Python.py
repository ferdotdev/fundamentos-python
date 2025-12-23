"""
Una variable es una espacio en memoria donde guardamos un valor para usarlo después. 
Con el signo igual (“=” es el operador de asignación) definimos el nombre y asignamos el valor

Consideraciones importantes

- Con print no se imprime el nombre de la variable, sino su valor.
- Python permite sobreescribir variables según el orden del código.
- Python es case sensitive variables con el mismo nombre pero en mayúsculas y minúsculas seran diferentes.
"""

# Asignación básica
x = "New variable"
print(x)  # Imprime: New variable

# Reasignación (sobreescritura)
x = "Overwriting x"
print(x)  # Imprime: Overwriting x

# Case sensitive
x = "lowercase"
X = "uppercase"
# Ambas imprimen valores diferentes
print(x)  # lowercase
print(X)  # uppercase