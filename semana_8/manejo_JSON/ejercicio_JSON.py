"""2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo."""

import json
#2)Cree un programa que permita agregar un Pokémon nuevo .
"""
1. Debe leer el archivo para importar los Pokémones existentes.
2. Luego debe pedir la información del Pokémon a agregar.
3. Finalmente debe guardar el nuevo Pokémon en el archivo.
"""

def read_json_file(path):#de json a python
    with open(path,'r') as file :
        reader = json.load(file)
    return reader


def create_pokemon(list_pokemones):
    while True:
      try:      
          name = input('Digite el nombre del pokemon:')
          check_valid_entry(name)
          
          type = input('Digite el tipo del pokemon:')
          check_valid_entry(type)
          
          health_points = input('Digite los puntos de salud del pokemon:')
          check_numeric_entry(health_points)
          
          attack=input('Digite el nivel de ataque:')
          check_numeric_entry(attack)
          
          defense=input('Digite el nivel de defensa:')
          check_numeric_entry(defense)
          
          special_attack =input('Digite el nivel de ataque especial:')
          check_numeric_entry(special_attack)
          
          special_defense =input('Digite el nivel de defensa especial:')
          check_numeric_entry(special_defense)
          
          speed = input('Ingrese la velocidad:')
          check_numeric_entry(speed)
          

          new_pokemon = {
            "name": {
              "english": name 
            },
            "type": [
              type
            ],
            "base": {
              "HP": health_points,
              "Attack": attack,
              "Defense": defense,
              "Sp. Attack": special_attack,
              "Sp. Defense": special_defense,
              "Speed": speed 
            }
          }

          list_pokemones.append(new_pokemon)
          return list_pokemones
      
      except Exception as e:
        print(f'Se ha producido un error {e}')


def check_valid_entry(type):
    if not type.isalpha():
      raise ValueError('Valor incorrecto solo puede ingresar letras o dejo el campo vacio.')
      print('Intentelo de nuevo!')
      

def check_numeric_entry(value):
    if not value.isdigit():
      raise ValueError('Valor incorrecto solo puede ingresar numeros o dejo el campo vacio.')
      print('Intentelo de nuevo!')


def write_json_file(path, updated_list):
    with open(path,'w') as file:
      json.dump(updated_list,file,indent="")


def main():
    try:
      path = r'Semana_8\manejo_JSON\pokemones.json'
      list_pokemones= read_json_file(path) #me da la lista
      updated_list = create_pokemon(list_pokemones)
      write_json_file(path, updated_list)
      print('Pokemon agregado con exito!')
    except Exception as e:
        print(f'Se ha producido un error {e}')


if __name__ == '__main__':
    main()