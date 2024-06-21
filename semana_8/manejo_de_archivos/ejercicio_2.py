"""2)Cree un programa que lea nombres de canciones de un archivo 
(línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente."""

def get_songs_line_by_line(path):
    sorted_line=[]
    with open(path,'r') as f1:
        for line in f1.readlines():
            sorted_line.append(line)
    sorted_line.sort()
    return sorted_line


def sorted_songs(path,songs):
    with open(path, 'w') as f2:
        f2.writelines(songs)


def main():
    songs_path = 'semana_8\\manejo_de_archivos\\canciones.txt'
    sorted_songs_path = 'semana_8\\manejo_de_archivos\\canciones_ordenadas.txt'
    songs = get_songs_line_by_line(songs_path)
    sorted_songs(sorted_songs_path,songs)


if __name__ == '__main__':
    main()
