"""  
5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
"""


#***************DEFINCION DE LAS VARIABLES************

cantidad_notas = int(input("Ingrese la cantidad de notas del estudiante : "))
count = 0
cantidad_notas_aprobadas = 0
cantidad_notas_desaprobadas = 0
suma_notas_aprobadas= 0
suma_notas_desaprobadas = 0
suma_todas_notas = 0
promedio_notas_desaprobadas = 0
promedio_notas_aprobadas = 0
promedio_todas_notas = 0



#CICLO WHILE 

while (count < cantidad_notas):
    nota=int(input(f"Ingrese la nota # {count+1} : "))

    if(nota >= 70):
        cantidad_notas_aprobadas = cantidad_notas_aprobadas + 1
        suma_notas_aprobadas = suma_notas_aprobadas + nota
        
    else:
        cantidad_notas_desaprobadas = cantidad_notas_desaprobadas + 1
        suma_notas_desaprobadas = suma_notas_desaprobadas + nota
        #print("cantidad de notas desaprobadas: ", cantidad_notas_desaprobadas)
    
    count= count+1
    

if(cantidad_notas_aprobadas>0):
    promedio_notas_aprobadas = suma_notas_aprobadas/cantidad_notas_aprobadas
else:
    promedio_notas_aprobadas = 0

if(cantidad_notas_desaprobadas>0):
    promedio_notas_desaprobadas = suma_notas_desaprobadas/cantidad_notas_desaprobadas
else:
    promedio_notas_desaprobadas = 0

suma_todas_notas = suma_notas_aprobadas+suma_notas_desaprobadas
promedio_todas_notas = suma_todas_notas / cantidad_notas

print(f"La cantidad de notas aprobadas es la siguiente : {cantidad_notas_aprobadas} y la cantidad de notas desaprobadas es : {cantidad_notas_desaprobadas}")
print(f"El promedio de  las notas aprobadas es : {promedio_notas_aprobadas}")
print(f"El promedio de las notas desaprobadas es: {promedio_notas_desaprobadas}")
print(f"El promedio de todas las notas es : {promedio_todas_notas}")
