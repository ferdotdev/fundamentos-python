# Operadores de asignacion

x = 100    # Asignacion inicial
x = x + 3  # Asignacion simple
x += 3     # Asignacion con operador de suma
x -= 2     # Asignacion con operador de resta
x *= 4     # Asignacion con operador de multiplicacion
x /= 2     # Asignacion con operador de division
x %= 3     # Asignacion con operador de modulo
print(x)

y = 5
y //= 2    # Asignacion con operador de division entera
y **= 3    # Asignacion con operador de potencia

# Operador walrus
print(y := 2) 

print(y)