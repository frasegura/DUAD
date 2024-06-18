# 6.1. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def convert_string_to_list(new_string):
    #print(new_string)
    mi_lista =[]
    palabra =""
    for i in new_string:
        if i != '-':
            palabra +=i      
        else:
            mi_lista.append(palabra)
            palabra =""
    mi_lista.append(palabra)
    return mi_lista
    

def order_list(mi_lista):
    for i in range(len(mi_lista)): #0-4  2
        for j in range(len(mi_lista)-1):#0-3   
            if mi_lista[j]>mi_lista[j+1]:
                mi_lista[j],mi_lista[j+1] =  mi_lista[j+1],mi_lista[j]

    return mi_lista
    

def convert_list_to_string(mi_lista):
    palabras_ordenadas = '-'.join(mi_lista)
    print(palabras_ordenadas)


mi_string ="python-variable-funcion-computadora-monitor"
string_to_list =convert_string_to_list(mi_string)
ordered_list = order_list(string_to_list)
convert_list_to_string(ordered_list)
