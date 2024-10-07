import pytest
from ejercicio_2 import get_numbers
# Function : get_numbers()
#Test con parametros que no sean int values y excepcion
#Test con valores repetidos
#Test con numeros que no son primos y arroje lista vacia

def test_get_numbers_incorrect_paramaters():
    #Arrange, act, assert
    my_input = 'abcde'
    with pytest.raises(ValueError):
        get_numbers(my_input)

def test_get_numbers_repeated_values():
    my_input = [2,2,3,5,8]
    result = get_numbers(my_input)
    assert  result == [2,2,3,5]

def test_get_numbers_non_prime_numbers():
    my_input = [1,4,6,18]
    result = get_numbers(my_input)
    assert  result == []



