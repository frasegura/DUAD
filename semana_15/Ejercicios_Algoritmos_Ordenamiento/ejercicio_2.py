#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def sorted_bubble_sort(new_list):
    for i in range(len(new_list)-1,0,-1):
        for j in range(len(new_list)-1,0,-1):
            print(i,j,':' ,new_list)
            if new_list[j-1] > new_list[j] :
                #print(f'cambio de posiciones : {new_list[j-1]} y {new_list[j]}  ')
                new_list[j-1], new_list[j]  = new_list[j] , new_list[j-1]
            
my_list = [4,2,5,1,0]
sorted_bubble_sort(my_list)
print(f'Sorted list : {my_list}')
