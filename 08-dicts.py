### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Rodrigo", "Apellido": "Ramirez", "Edad": 21, 1: "Python"}

my_dict = {
    "Nombre": "Rodrigo",
    "Apellido": "Ramirez",
    "Edad": 21,
    "Lenguajes": {"Python", "Javascript", "Java", "C#"},
    1: 1.74
}

# print(my_other_dict)
# print(my_dict)

# print(len(my_other_dict))
# print(len(my_dict))

# # Búsqueda

# print(my_dict[1])
# print(my_dict["Nombre"])

# print("Rodrigo" in my_dict)
# print("Apellido" in my_dict)

# # Inserción

# my_dict["Calle"] = "Calle Principal"
# print(my_dict)

# # Actualización

# my_dict["Nombre"] = "Salvador"
# print(my_dict["Nombre"])

# # Eliminación

# del my_dict["Calle"]
# print(my_dict)

# Otras operaciones

# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Rodrigo")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))
print(my_values)

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))