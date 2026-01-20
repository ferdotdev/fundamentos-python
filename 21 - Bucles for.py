palabra = 'Python'

for letra in palabra:
    print(letra)

for letra in palabra:
    if letra == 'y':  # Nota: Python es sensible a mayúsculas y minúsculas
        break
    print(letra)


frutas = ['Manzana', 'Banana', 'Cereza']

for fruta in frutas:
    print(fruta)

for fruta in frutas:
    if fruta == 'Banana':
        continue
    print(fruta)
else:
    print('Bucle finalizado')


print('-------------------------')

for i in range(0,10,2):
    print(i)

models = ['ChatGPT', 'Claude', 'Gemini']
apps = ['is awesome', 'is cool']

for model in models:
    for app in apps:
        print(model, app)

frutas = ["manzana", "naranja", "kiwi"]
adjetivos = ["rica", "saludable"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)


frutas = ["manzana", "naranja", "kiwi"]
adjetivos = ["rica", "saludable"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)

'''
Porque funciona, al invertirlo lo que creas es que primero el bucle frutas, pase por el
bucle adjetivos
'''

for i in range(2):
    pass