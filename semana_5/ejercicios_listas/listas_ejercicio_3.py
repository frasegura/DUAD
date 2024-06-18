#3)Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

color_list = [
    "grey",
    "blue",
    "yellow",
    "black",
    "green",
    "white",
    "brown"
]

first_value = color_list[0]
last_value =color_list[len(color_list)-1]

color_list.pop(0)
color_list.pop(len(color_list)-1)

color_list.insert(0,last_value)
color_list.insert(len(color_list),first_value)
print(color_list)
