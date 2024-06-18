#2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño,
# preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

nombre_usuario = input("Ingrese el nombre del usuario:")
apellido_uusario = input("Ingrese el apellido del usuario:")
edad_usuario = int(input("Ingrese la edad del usuario :"))

#bebe:edades: 1-5 años
#nino:edades de 6 a 10 años
#preadolescente edades de 11 a 13  años
#adolescente edades de 14 a 17 años
#adulto joven edades de 18 35 años
#adulto edades de 36 a 50 años
#adulto mayor edades de 51 años en adelante

if(edad_usuario <=5):
    print(f"{nombre_usuario} {apellido_uusario} es un bebe")
elif(edad_usuario<=10):
     print(f"{nombre_usuario} {apellido_uusario} es un(a) nino(a)")
elif(edad_usuario <= 13):
     print(f"{nombre_usuario} {apellido_uusario} es un(a) preadolescente")  
elif(edad_usuario <=17 ):
     print(f"{nombre_usuario} {apellido_uusario} es un(a) adolescente ")
elif(edad_usuario <=35):
      print(f"{nombre_usuario} {apellido_uusario} es un(a) adulto(a) joven ")
elif(edad_usuario<=50):
     print(f"{nombre_usuario} {apellido_uusario} es un(a) adulto(a)")
else :
     print(f"{nombre_usuario} {apellido_uusario} es un(a) adulto(a) mayor")
