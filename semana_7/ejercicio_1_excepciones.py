
"""Cree una calculadora por linea de comando. Esta debe de tener 
un número actual, y un menú para decidir qué operación hacer con otro número"""

# Calculadora  V2


def  desplegar_menu():
    valor_actual = 0
    opcion = 0
    while opcion!=6:
        try:
            selected_option = input('Ingrese la opcion que desea: 1.Suma  2. Resta 3. Multiplicación 4. División  5. Borrar resultado 6.Salir. Opcion seleccionada : ')
            check_numeric_option_selected(selected_option)
            opcion = int(selected_option)
            check_option(opcion)
            
            if opcion == 1:
                valor_actual = suma(valor_actual)
                print(valor_actual)
            elif opcion ==2:
                valor_actual = resta(valor_actual)
                print(valor_actual)
            elif opcion == 3:
                valor_actual = multiplicacion(valor_actual)
                print(valor_actual)
            elif opcion == 4:
                valor_actual = division(valor_actual)
                print(valor_actual)
            elif opcion == 5:
                valor_actual = borrar_resultado()
                print(valor_actual)

        except ValueError as e:
            print(f'Se ha producido un error : {e}')


def check_numeric_option_selected(selected_option):
    if not selected_option.isdigit():
        raise ValueError('Opcion invalida, no se pueden letras o simbolos')


def check_option(selected_option):
    if selected_option < 1 or selected_option > 6:
        raise ValueError('Opcion invalida')


def suma(valor_actual):
    valor_ingresado = input('Ingrese un valor:')
    if not valor_ingresado.isdigit():
        raise ValueError('Ingrese valores numericos para las operaciones')
    else:
        valor_actual+=float(valor_ingresado)
        return valor_actual


def resta(valor_actual):
    valor_ingresado = input('Ingrese un valor:')
    if not valor_ingresado.isdigit():
        raise ValueError('Ingrese valores numericos para las operaciones')
    else:
        valor_actual-=float(valor_ingresado)
        return valor_actual


def multiplicacion(valor_actual):
    valor_ingresado =input('Ingrese un valor:')
    if not valor_ingresado.isdigit():
        raise ValueError('Ingrese valores numericos para las operaciones')
    else:
        valor_actual*=float(valor_ingresado)
        return valor_actual


def division(valor_actual):
    valor_ingresado = input('Ingrese un valor:')
    try:
        if not valor_ingresado.isdigit():
            raise ValueError('Ingrese valores numericos para las operaciones')
        else:
            valor_actual/=float(valor_ingresado)
            return valor_actual
    except ZeroDivisionError:
        print('No se permite la division entre 0')
        return valor_actual


def borrar_resultado():
    valor_borrado = 0
    return valor_borrado


def main():
    try:
        desplegar_menu()
    except Exception as e:
        print(f'Se ha producido un error {e}')


if __name__ == '__main__':
    main()

