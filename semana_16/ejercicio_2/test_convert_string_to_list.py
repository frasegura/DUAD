import pytest
from ejercicio_2 import convert_string_to_list,get_ordered_string

#Function convert_string_to_list ,get_ordered_string

#6.Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#Test con string vacios
#Test con lista ya ordenada
#test con palabras repetidas

def test_get_ordered_empty_string():
    #AAA
    my_input = ''
    result = get_ordered_string(my_input)
    assert result == ''

def test_get_ordered_string_already_ordered():
    my_input = 'arriba-boleta-casa-zanahoria'
    result = get_ordered_string(my_input)
    assert result.strip() == 'arriba-boleta-casa-zanahoria'