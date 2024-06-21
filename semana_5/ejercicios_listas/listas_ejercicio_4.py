#4)Cree un programa que elimine todos los números impares de una lista.

number_list = [1,2,3,4,5,6,7,8,9]
#9-1 = 0-8 
for i in range(len(number_list)-1,-1,-1):
    if number_list[i] %2 == 1:
        number_list.pop(i)      
print(number_list)
