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