"""2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)"""

#3.Cree una función que retorne la suma de todos los números de una lista.
def sum_list_numbers(my_list):
    if not isinstance(my_list,list):
        raise ValueError('The parameter must be a list') 
    else:
        suma = 0
        for data in my_list:
            if not isinstance(data,int):
                raise ValueError('The values within the list must be int values')
            else:
                pass

        for i in my_list:
            suma += i
        return suma

#4.Cree una función que le de la vuelta a un string y lo retorne.
def get_inverted_string(my_string):
    if not isinstance(my_string,str):
        raise ValueError('The parameter must be a string')
    new_word = ''
    for i in range(len(my_string)-1,-1,-1): # Hola
        new_word+= my_string[i]
    return new_word

#5.Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
def count_lower_and_upper(my_string):
    if not isinstance(my_string,str):
        raise ValueError('The parameter must be a string')
    else:
        lower_count = 0
        upper_count = 0
        for i in my_string:
            if i.isupper():
                upper_count +=1
            elif i.islower():
                lower_count +=1
        return f'Upper case count: {upper_count} , lower case count: {lower_count}'

#6.Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
def convert_string_to_list(new_string):
    my_list = []
    word = ''
    for i in new_string:
        if i != '-':
            word += i
        else:
            my_list.append(word)
            word =""
    my_list.append(word)
    return my_list

def get_ordered_string(my_string):
    new_list = convert_string_to_list(my_string)
    for i in range(len(new_list)-1):
        for j in range(len(new_list)-1):
            if new_list[j] > new_list[j+1]:
                new_list[j] ,new_list[j+1] = new_list[j+1] ,new_list[j]
    return '-'.join(new_list)

#7.Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
def  get_numbers(number_list):
    lista_primos =[]
    for i in number_list:
        if not isinstance(i,int):
            raise ValueError('The values within the list must be integers')
        else:
            if i==2:
                lista_primos.append(i)
            else:
                for j in range(2,i):
                    if i%j == 0:
                        #print(f"{i}no es primo") 
                        break                        
                    elif j == i-1:
                        #print(f"{i}  es primo")
                        lista_primos.append(i)
                        
    return lista_primos



    
if __name__ == '__main__':
    print(f'Sum list : {sum_list_numbers([1,2,3,4])}')
    get_inverted_string('Hola')
    count_lower_and_upper('Hola mi nombre es hola mundo')
    get_ordered_string('hola-mundo-gato-perro')
    prime_number = get_numbers([1,3,5, 4, 6, 7, 13, 9, 67])
    print(f'Prime numbers : {prime_number}')


    
