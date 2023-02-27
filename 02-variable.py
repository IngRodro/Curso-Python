# Variables


my_string_variable = "My String Variable"
print(my_string_variable)

# Integers
my_int_variable = 5
print(my_int_variable)

# Convertir un entero a string
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Booleanos
my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este se el valor de my_string_variable:", my_string_variable)

# Funcion len
print(len(my_string_variable))

# Variables en una sola linea
first_name, last_name, alias, age = "Rodrigo", "Ramirez.", "IngRodro.", 21
print("Me llamo:", first_name, last_name,"Mi alias es:", alias, "Y mi edad es:" , age)


# Inputs
"""first_name = input("¿Cual es tu nombre? ")
last_name = input("¿Cual es tu apellido? ")
age = input("¿Cual es tu edad? ")
print("Tu nombre es:", first_name, last_name)
print("Tu edad es:", age)
"""

# ¿Forzamos el tipo de dato?
address: str = 32
address = 32
print(type(address))