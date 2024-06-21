# 3)Cree un programa que use una lista para eliminar keys de un diccionario.

mi_lista = ["nombre","edad"]
mi_diccionario ={
    "nombre": "Luke",
    "apellido": "Skywalker",
    "edad":25,
    "profesion":"piloto"
}
print(mi_diccionario)

for keys_lista in mi_lista :
    #print(keys_lista)
    if keys_lista in mi_diccionario:
        mi_diccionario.pop(keys_lista)
print(mi_diccionario)