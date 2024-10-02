import pytest
from ejercicio_2 import  get_inverted_string

#Function get_inverted_string()

#que solo acepte strings
#que los strings no sean mayor a 10 letras
#que los stings no sean menores a 2 letras

def test_get_inverted_string_only_strings():
    #AAA
    #Arrange
    my_input = 1234    
    #Act and Assert
    with pytest.raises(ValueError):
        get_inverted_string(my_input)

def test_get_inverted_string_max_amount():
    #AAA
    #Arrange
    my_input = 'abecedario'
    #Act
    result = get_inverted_string(my_input)
    #Assert
    assert len(result) <= 10

def test_get_inverted_string_min_amount():
    #AAA
    #Arrange
    my_input = 'a'
    #Act
    result = get_inverted_string(my_input)
    #Assert
    assert len(result) >= 1

    


