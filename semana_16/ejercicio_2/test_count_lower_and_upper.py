import pytest
from ejercicio_2 import count_lower_and_upper

#Function count_lower_and_upper

#Test solo string values
#Test con cadena vacia
#Test con solo Mayusculas

def test_count_lower_and_upper_only_string_values():
    #AAA
    #Arrange
    my_input = 5
    #Act and Assert
    with pytest.raises(ValueError):
        count_lower_and_upper(my_input)

def test_count_lower_and_upper_empty():
    #AAA
    my_input = ''
    result = count_lower_and_upper(my_input)
    assert result.strip() == 'Upper case count: 0 , lower case count: 0'

def test_count_lower_and_upper_only_upper_case():
    #AAA
    my_input = 'HELLO WORLD'
    result = count_lower_and_upper(my_input)
    assert result.strip() == 'Upper case count: 10 , lower case count: 0'