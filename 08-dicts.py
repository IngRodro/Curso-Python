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

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Rodrigo" in my_dict)
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle Principal"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Salvador"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)
