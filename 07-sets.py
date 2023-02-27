# ### Sets ###

# my_set = set()
# my_other_set = {}

# print(type(my_set))
# print(type(my_other_set))  # Inicialmente es un diccionario

# my_other_set = {21, 1.74, "Rodrigo", "Ramirez"}
# print(type(my_other_set))

# print(len(my_other_set))

# my_other_set.add("IngRodro") # Un set no es una estructura ordenada
# print(my_other_set)

# my_other_set.add("Rodrigo") # Un set no permite elementos duplicados
# print(my_other_set)

# # Busqueda
# print("Rodrigo" in my_other_set)
# print("Salvador" in my_other_set)

# # Eliminación
# my_other_set.remove("Rodrigo")
# print(my_other_set)

# my_other_set.discard("IngRodro")
# print(my_other_set)

# my_other_set.discard("Salvador") # No genera error si el elemento no existe
# print(my_other_set)

# # my_other_set.remove("Salvador") # Genera error si el elemento no existe
# # print(my_other_set)

# my_other_set.clear()
# print(my_other_set)
# print(len(my_other_set))

# # Operaciones con sets
# my_set = {1, 2, 3, 4, 5}
# my_other_set = {4, 5, 6, 7, 8}

# del my_other_set
# # print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Rodrigo", "Ramirez", 21}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Javascript", "Java", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Kotlin", "C#"}))
print(my_new_set.difference(my_set))