""" 1. Cree una clase de `Circle` con:
    1. Un atributo de `radius` (radio).
    2. Un método de `get_area` que retorne su área. """

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    
    def get_area(self):
        area = 3.14*(self.radius**2)
        return area

my_circle = Circle(5)
print(my_circle.get_area())