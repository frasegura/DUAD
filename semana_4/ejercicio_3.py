#3. Cree un programa con un numero secreto del 1 al 10. 
#El programa no debe cerrarse hasta que el usuario adivine el numero.
numero_secreto = int(input("Por favor digite el numero secreto : "))

numero_adivinado = False

while(not numero_adivinado):
    numero_usuario = int(input("Por favor ingrese el numero e intente adivinar : "))

    if(numero_usuario == numero_secreto):
        print("Felicicades has adivinado el numero!")
        numero_adivinado = True
    elif(numero_usuario != numero_secreto):
        print("El numero ingresado es incorrecto por favor intentelo de nuevo.")
        numero_adivinado = False
