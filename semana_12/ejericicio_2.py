"""2. Cree una clase abstracta de `Shape` que:
    1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
    2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
    3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro."""
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2*3.14*self.radius
    
    def calculate_area(self):
        return 3.14*(self.radius^2)

class Square(Shape):
    def __init__(self,side):
        super().__init__()
        self.side = side

    def calculate_perimeter(self):
        return 4*self.side

    def calculate_area(self):
        return self.side*self.side

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return 2*(self.length+self.width)
    
    def calculate_area(self):
        return self.length*self.width
    

my_circle = Circle(5)
print('CIRCLE: ')
print('* Circumference of circle :', "{:.2f}".format(my_circle.calculate_perimeter()))
print('* Area of circle : ', my_circle.calculate_area())

print('SQUARE: ')
my_square = Square(2)
print('* Perimiter of a square : ', my_square.calculate_perimeter())
print('* Area of a square : ', my_square.calculate_area())

print('RECTANGLE: ')
my_rectangle = Rectangle(6,3)
print('* Perimiter of a rectangle : ', my_rectangle.calculate_perimeter())
print('* Area of a rectangle : ', my_rectangle.calculate_area())