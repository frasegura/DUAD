import unittest
import random
from  ejercicio_1  import sorted_bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_bubble_sort_sort_a_short_list_correctly(self):
        #AAA
        #Arrange
        list_input = [3,1,8]
        #Act
        result = sorted_bubble_sort(list_input)
        #print(sorted(list_input))
        #print(result)
        #Assert
        self.assertEqual(result, sorted(list_input))

    def test_sorted_bubble_sort_sort_a_long_list_correctly(self):
        #AAA
        #Arrange
        new_list = [random.randint(0,100) for _ in range(100)] #GENERAR NUMEROS RANDOM BUSCAR FUNCION  
        #Act    
        result = sorted_bubble_sort(new_list)
        #Assert
        self.assertEqual(result, sorted(new_list))

    def test_sorted_bubble_sort_empty_list(self):
        #AAA
        #Arrange
        new_list = []
        #Act
        result = sorted_bubble_sort(new_list)
        #Assert
        self.assertEqual(result,[])

    def test_sorted_bubble_sort_non_list_parameters(self):
        #Arrange
        parameter = 3
        #Act and Assert
        with self.assertRaises(ValueError):
            sorted_bubble_sort(1)
        

if __name__ == '__main__':
    unittest.main()

