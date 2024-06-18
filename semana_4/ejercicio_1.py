#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

# 1. string + string → ?
print("****# 1. string + string → ?***** ")
nombre = 'Francisco'
apellido = ' Segura'

print(nombre + apellido)

# 2. string + int → ?
print("****# 2. string + int → ?**** ")

marca = 'Toyota '
annio = 2023


print(marca + str(annio))

# 3. int + string → ?
print("****# 3. int + string → ?****")

motor = 1600
modelo = ' Yaris'

print(str(motor) +  modelo)


# 4. list + list → ?
print("****# 4. list + list → ?*****")

lista_1 = [1,2,3,4]
lista_2 = [5,6,7,8]

print(lista_1 + lista_2)

# 5. string + list → ?
print("****# 5. string + list → ?*****")
equipo = 'Barcelona'
lista_3 = ['Dortmund','Ajax', 'Manchester']

print(equipo + "  ".join(lista_3))


# 6. float + int → ?
print("***# 6. float + int → ?***")

numero_float = 3.2
numero_int = 8

print(numero_int +numero_float)

# 7. bool + bool → ?
print("****# 7. bool + bool → ?***")

booleano_1 = False
booleano_2 = False
print(" False + False : ")
print(booleano_1 + booleano_2)

print(" True + False : ")
booleano_3 = True
booleano_4 =  False 
print(booleano_3+booleano_4)

print(" True + True : ")
booleano_5 = True
booleano_6 = True
print(booleano_5+booleano_6)