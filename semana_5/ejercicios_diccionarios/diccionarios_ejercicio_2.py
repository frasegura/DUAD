# 2)Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

key_list = ["primer_numero","segundo_numero","tercer_numero","cuarto_numero"]
number =[21,322,33,55]
dictionary = dict()
#dictionary = {}
for i in range (len(key_list)):
    dictionary[key_list[i]]=number[i]
print(dictionary)

#pba con zip
pba_dict = dict(zip(key_list,number))
print(f"Esta es una prueba con zip:{pba_dict}")