"""1)Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.

1. Debe incluir:
    1. Nombre
    2. Género
    3. Desarrollador
    4. Clasificación ESRB"""

#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
import csv

def write_games_into_csv_file(path,data,headers):
    with open(path,'w',encoding='UTF-8') as file:
        writer = csv.DictWriter(file,fieldnames=headers) 
        writer.writeheader()
        writer.writerows(data)


def get_games():
    while True:
        games_dict = {}
        print('------------------')
        try:
            games_dict['nombre'] = input(f'Ingrese el nombre del juego :')
            games_dict['genero']  =  input(f'Ingrese el genero del juego :')
            games_dict['desarrollador']  =  input(f'Ingrese el desarrollador del juego :')
            games_dict['clasificacion']  = input(f'Ingrese la clasificacion ESRB del juego  :')
            games_clasification =  games_dict['clasificacion']      
            check_clasification(games_clasification)

            return games_dict
        except ValueError as e:
            print(f'Se ha producido un error {e}')
            print(f'Vuleva a ingresar la informacion')


def  check_clasification(game_clasification):
    if not game_clasification.isalpha():
        raise ValueError('Para la clasificacion ingrese un valor valido(solo letras)')

def check_number_games(games_number):
    if not games_number.isdigit():
        raise ValueError('Ingrese un valor valido, solo valores numericos')
        return False


def main():
    game_number_is_true = True
    while game_number_is_true:
        try:
            games_number = input('Ingrese la cantidad de juegos: ')
            game_number_is_true = check_number_games(games_number)
            n = int(games_number)
            games_list = []
            games_headers =('nombre','genero','desarrollador','clasificacion')
            games_path = r'Semana_8\manejo_CSVs\games.csv'
            for i in range(n):
                games_info = get_games()
                games_list.append(games_info)

            write_games_into_csv_file(games_path,games_list,games_headers)
            print('Los juegos se han agregado correctamente.')
        
        except Exception as e:
            print(f'Se ha producido un error {e}')


if __name__ =='__main__':
    main()


