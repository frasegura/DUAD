#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


def check_parameters(func):
    def wrapper(new_list):
        print('Reviewing function parameters...')
        for i in new_list:
            if not i.isdigit():
                raise ValueError('To get the total the list only can contain numbers')            
        func(new_list)
            
    return wrapper

@check_parameters
def sum_func(new_list):
    result = 0
    for i in new_list:
        result = result + int(i)
    print(result)


def main():
    cont = True
    new_list = []
    while cont:
        number = input('Please enter a number : ')
        new_list.append(number)
        print(new_list)
        cont = input('Do you want  to continue  ? (yes/no) : ')=='yes'

    sum_func(new_list)




if __name__ == '__main__':
    main()