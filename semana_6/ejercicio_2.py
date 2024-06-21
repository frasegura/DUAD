"""2 .Experimente con el concepto de scope:

1. Intente accesar a una variable definida dentro de una función desde afuera.
2.  Intente accesar a una variable global desde una función y cambiar su valor."""

#2.1 Intente accesar a una variable definida dentro de una función desde afuera.
def define_function():
    intern_var = [1,2,3]
    return intern_var

#print (intern_var) #NameError: name 'intern_var' is not defined  , no permite accesarla desde afuera


#2.2  Intente accesar a una variable global desde una función y cambiar su valor.

global_variable = "Esta es una variable global"

print(f"Este es el valor de la variable global antes de ejecutar la funcion :{global_variable}")

def change_global_variable():
    global_variable = "Ha cambiado su valor dentro de la funcion"
    #return global_variable
    print(global_variable)


#print (change_global_variable())
change_global_variable()
#print (global_variable)