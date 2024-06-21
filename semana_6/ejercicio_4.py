# 4.Cree una función que le de la vuelta a un string y lo retorne.

def inverted_string(new_string):
    new_word = ''
    for i in range(len(new_string)-1,-1,-1):
        new_word += new_string[i]

    print(new_word)


my_string = input("Por favor ingrese una palabra :")
inverted_string(my_string)