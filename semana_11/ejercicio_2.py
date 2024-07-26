"""2. Cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro).
      **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno."""

class Person:
    def __init__(self,name) :
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
        
    
    def add_passengers(self,passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f'A passenger called {passenger.name} was added')
        else:
            print('The list is full')

    def remove_passengers(self):
        if self.passengers:
            removed_passenger = self.passengers.pop()
            print(f'A passenger called {removed_passenger.name} was removed from the bus list')
        else:
            print('The bus list is empty')

my_bus = Bus(4)
passenger_1 = Person('Leo')
passenger_2 = Person('Maria')
passenger_3 = Person('Laura')

my_bus.add_passengers(passenger_1)
my_bus.add_passengers(passenger_2)
my_bus.add_passengers(passenger_3)

my_bus.remove_passengers()