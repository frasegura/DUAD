"""1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
    1. Funciona con una lista pequeña.
    2. Funciona con una lista grande (de más de 100 elementos.
    3. Funciona con una lista vacía.
    4. No funciona con parámetros que no sean una lista."""


def sorted_bubble_sort(new_list):
    if not isinstance(new_list,list ):
        raise ValueError('This parameter is not a list')
    
    
    for i in range(len(new_list)-1):
        has_made_changes = False
        for j in range(len(new_list)-1-i):
            if new_list[j] > new_list[j+1]:
                new_list[j] , new_list[j+1] = new_list[j+1], new_list[j] 
                has_made_changes = True

        if not has_made_changes:
            break

    return new_list
        

my_list = [11,88,6,4,12,222,0,1]
result = sorted_bubble_sort(my_list)
print(f'Sorted list : {result}')

