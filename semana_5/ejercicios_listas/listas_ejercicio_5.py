# 5)Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

tamano_lista = 10
mi_lista = [] # 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 

for i in range(tamano_lista):
    numero_usuario = int(input("Por favor ingrese un numero para anadirlo a la lista: "))
    mi_lista.append(numero_usuario)
numero_mayor=mi_lista[0]
for numero_lista in mi_lista:
    print(numero_lista)
    if(numero_lista >numero_mayor):
        numero_mayor=numero_lista

print(f"{mi_lista} y el numero mayor es : {numero_mayor}")