#Analice el algoritmo de bubble_sort usando la Big O Notation.

def sorted_bubble_sort(new_list): # O(n^2)
    for i in range(len(new_list)-1):# O(n)
        has_made_changes = False # O(1)
        for j in range(len(new_list)-1-i): # O(n^2)
            print(f'Iteracion :{i}, {j}. Valor actual {new_list[j]} , Valor siguiente : {new_list[j+1]}') # O(1)
            if new_list[j] > new_list[j+1]: # O(1)
                new_list[j] , new_list[j+1] = new_list[j+1], new_list[j] # O(1)
                has_made_changes = True # O(1)
                print(f'Position change has been made: {has_made_changes}') # O(1)
        print(has_made_changes) # O(1)

        if not has_made_changes: # O(1)
                return # O(1)

my_list = [11,88,6,4,12,222,0,1] # O(1)
sorted_bubble_sort(my_list) # O(n^2)
print(f'Sorted list : {my_list}') #  O(1)
