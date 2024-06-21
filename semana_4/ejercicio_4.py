#Cree un programa que le pida tres números al usuario y muestre el mayor.

numero_1 = int(input("Ingrese el primer numero:"))
numero_2 = int(input("Ingrese el segundo numero:"))
numero_3 = int(input("Ingrese el tercer numero:"))

if(numero_1 > numero_2):
    print(f"El numero {numero_1} es el mayor.")
elif(numero_1>numero_3):
 print(f"El numero {numero_1} es el mayor.")
elif(numero_2 > numero_3):
    print(f"El numero {numero_2} es el mayor.")
else:
    print(f"El numero {numero_3} es el mayor.")