#7.Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def get_pair_numbers(number_list):
    lista_primos =[]
    for i in number_list:
    #print(i)
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


lista_numeros = [1,49,2,3,5, 4, 6, 7, 13, 9, 67]
print(get_pair_numbers(lista_numeros))