### Strings ###

my_string = "Mi String"
# my_other_string = 'Mi otro string'

# # Tamaño de un string
# print(len(my_string))
# print(len(my_other_string))

# # Concatenación de strings
# print(my_string + my_other_string)
# print(my_string + " " + my_other_string)

# Escapar caracteres

# # Comillas dobles
# print("Hola \"Mundo\"")
# # Comillas simples
# print('Hola \'Mundo\'')
# # Salto de linea
# print("Este es \nsalto de linea")
# # Tabulador
# print("Este es \ttabulador")
# # Barra invertida
# print("Este es \\ barra invertida")


# # Indexación de strings
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[5])
print(my_string[6])
print(my_string[7])
print(my_string[8])

# Formateo de strings

name, last_name, age = "Rodrigo", "Ramirez", 21
print("Me llamo", name, last_name, "y tengo", age, "años")
print("Me llamo {} {} y tengo {} años".format(name, last_name, age))
print("Mi nombre es %s %s y tengo %d años" % (name, last_name, age))
print(f"Mi nombre es {name} {last_name} y tengo {age} años")

# # Slicing de strings

languaje = "Python"
print(languaje[1:3])
print(languaje[1:])
print(languaje[-2])
print(languaje[0:6:2])

## Reverse a string

reversed_languaje = languaje[::-1]
print(reversed_languaje)

# # Métodos de strings

# print(languaje.capitalize()) # Capitaliza el primer caracter
# print(languaje.upper()) # Convierte el string a mayusculas
# print(languaje.lower()) # Convierte el string a minusculas
# print(languaje.swapcase()) # Convierte el string a minusculas y mayusculas
# print(languaje.replace("o", "a")) # Reemplaza un caracter por otro
# print(languaje.count("o")) # Cuenta cuantas veces se repite un caracter
# print(languaje.startswith("Py")) # Verifica si el string empieza con un caracter
# print(languaje.endswith("on")) # Verifica si el string termina con un caracter
# print(languaje.isnumeric()) # Verifica si el string es numerico
# print("1".isnumeric()) # Verifica si el string es alfanumerico




