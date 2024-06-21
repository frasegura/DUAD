# 1)Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

lista_1 = [
    "cat",
    "dog",
    "fish",
    "rabbit"
]

lista_2 = [
    "black",
    "yellow",
    "red",
    "blue"
]

for i in range(len(lista_1)):
    print(lista_1[i], lista_2[i])