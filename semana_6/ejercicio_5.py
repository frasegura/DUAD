# 5.Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string

def count_upper_and_lower(new_string):
    count_upper = 0
    count_lower = 0
    for char in mi_string:
        if char.isupper():
            count_upper+=1
        elif char.islower() :
            count_lower+=1        
    print(f"There’s {count_upper} and {count_lower} lower cases")


mi_string = "I love Nación Sushi" 
count_upper_and_lower(mi_string)