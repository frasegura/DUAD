#2)Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import csv
#Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

def write_games_into_csv_file(path,data,headers):
    with open(path,'w',encoding='UTF-8') as file :
        writer = csv.DictWriter(file,fieldnames=headers, delimiter=' ')
        writer.writeheader()
        writer.writerows(data)

def get_games_info():
    while True :
        games_dict = {}
        print('------------------')
        try:
            games_dict['nombre'] =input('Ingrese el nombre del juego:')
            games_dict['genero'] = input('Ingrese el genero del juego:')
            games_dict['desarrollador'] = input('Ingrese el desarrollador del juego:')
            games_dict['clasificacion'] = input('Ingrese el clasificacion del juego:')
            games_clasification = games_dict['clasificacion']
            check_clasification(games_clasification)
            return games_dict
        except ValueError as e:
            print(f'Se ha producido un error {e}')

def check_clasification(games_clasification):
    if not games_clasification.isalpha():
        raise ValueError('Ingrese una clasificacion valida(solo letras)')


def check_number_games(games_number):
    if  not games_number.isdigit():
        raise ValueError('Ingrese un valor valido, solo valores numericos')
        return False

def main():
    game_number_is_true = True
    while game_number_is_true:
        try:           
            games_number = input('Ingrese la cantidad de juegos:')
            game_number_is_true = check_number_games(games_number)
            n=int(games_number)
            games_list= []
            game_path = r'Semana_8\manejo_CSVs\games_2.csv'
            games_headers =('nombre','genero','desarrollador','clasificacion')
            for i in range(n):
                info_games=get_games_info()
                games_list.append(info_games)
            
            write_games_into_csv_file(game_path,games_list,games_headers)
            print('Se han agregado los juegos correctamente.')
        except Exception as e:
            print(f'Se ha producido un error {e}')

if __name__ == '__main__':
    main()