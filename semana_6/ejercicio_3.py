# 3.Cree una función que retorne la suma de todos los números de una lista.

def sum_number_list(lista):
    suma=0
    for number in lista:
        suma += number
    print(f"El valor de la suma es:{suma}")


lista = [4, 6, 2, 29]
sum_number_list(lista)