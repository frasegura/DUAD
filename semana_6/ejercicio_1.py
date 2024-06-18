#1)Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_function_1():
    print("Esta es la primera funcion, que llamara a la segunda:")
    print_function_2()


def print_function_2():
    print("Esta es la segunda funcion.")


print_function_1()