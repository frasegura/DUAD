import pytest
from ejercicio_2 import sum_list_numbers

#Probar con pytest

# Function : sum_list_numbers
def test_sum_list_numbers_list_parameter_only():
    #AAA
    #Arrange
    my_input = 'Hola'
    #Act and Assert
    with pytest.raises(ValueError):
        sum_list_numbers(my_input)

def test_sum_list_numbers_less_than_100():
    #AAA
    #Arrange
    my_input = [1,2,3,89]    
    #Act
    result  = sum_list_numbers(my_input)
    #Assert
    assert result <= 100

def test_sum_list_numbers_list_elements_only_numbers():
    #AAA
    #Arrange
    my_input = [4,'a',2]
    #Act and Assert
    with pytest.raises(ValueError):
        sum_list_numbers(my_input)

