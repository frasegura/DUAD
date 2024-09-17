#Crea un bubble_sort por tu cuenta sin revisar el código de la lección.



def sorted_bubble_sort(new_list):
    for i in range(len(new_list)-1):
        has_made_changes = False
        for j in range(len(new_list)-1-i):
            print(f'Iteracion :{i}, {j}. Valor actual {new_list[j]} , Valor siguiente : {new_list[j+1]}')
            if new_list[j] > new_list[j+1]:
                new_list[j] , new_list[j+1] = new_list[j+1], new_list[j]
                has_made_changes = True
                #print(f'Position change has been made: {has_made_changes}')

        if not has_made_changes:
                return

my_list = [11,88,6,4,12,222,0,1]
sorted_bubble_sort(my_list)
print(f'Sorted list : {my_list}')
