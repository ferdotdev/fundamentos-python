import random

positivo = 5
negativo = -5
decimal = 3.14
decimal_negativo = -3.14
imaginario = 2 + 3j

# Type casting

integer = 1
floating = 1.1

castedInt = float(integer) + floating
print(castedInt)  # 2.1
print(type(castedInt))  # <class 'float'>

castedFloat = int(floating) + integer
print(castedFloat)  # 2
print(type(castedFloat))  # <class 'int'>

castedComplexInteger = complex(integer) + floating
print(castedComplexInteger)  # (2.1+0j)
print(type(castedComplexInteger))  # <class 'complex'>

castedComplexFloat = complex(floating) + integer
print(castedComplexFloat)  # (2.1+0j)
print(type(castedComplexFloat))  # <class 'complex'>

print(random.randrange(1, 11)) 