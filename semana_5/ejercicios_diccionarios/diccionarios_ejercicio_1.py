"""
Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones
El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
numero
piso
precio_por_noche

"""

dict_hotel = {
    "nombre":"Riu",
    "numero_de_estrellas" : 4,
    "habitaciones":[
        {
            "numero": 22,
            "piso": 2,
            "precio_por_noche": 120

        },
        {
            "numero": 66,
            "piso": 5,
            "precio_por_noche": 200
        },
        {
            "numero":89,
            "piso": 6,
            "precio_por_noche":250
        }    
    ] 
}

print(dict_hotel)