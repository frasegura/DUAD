#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def decorator_func(func):
    def wrapper(*args):
        print(f'The function name is : {func.__name__}')
        print(f'The function paremters are : {args} ')
        result = func(*args)
        print(f'The function : {result} ')
    return wrapper

@decorator_func
def sum_func(first_number,second_number):
    return first_number + second_number



def main():
    first_number = int(input('Please enter a number:'))
    second_number = int(input('Please enter a number:'))
    sum_func(first_number,second_number)

if __name__ == '__main__':
    main()