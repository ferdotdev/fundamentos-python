# Manipulacion de Strings en Python

# Acceso por índice
# Podemos acceder a caracteres individuales en un string usando indices
# Los indices empiezan en 0
text = "Python is dope"
print(text[5]) 

# Slicing
# Podemos obtener subcadenas usando slicing
# Estas tienen rangos de inicio a fin, donde el fin no esta incluido
# Siempre debemos añadir un indice extra al final
print(text[0:6]) 

# Replace

# Con replace podemos reemplazar contenido dentro de un string si 
# existe el contenido a reemplazar
content_course = "This course is about C#"
print(content_course.replace("C#", "Python"))

# Split
# Con split podemos dividir un string en una lista de strings
# usando un separador especifico
course_splited = content_course.split(" ")
print(course_splited)

# Normalize with case insensitive
# Podemos normalizar strings para hacer comparaciones sin importar
# mayusculas o minusculas
text = "HelLo WorLD"
wanted_word = "world"
print(wanted_word in text)
print(wanted_word.lower() in text.lower())