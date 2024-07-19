"""4. Cree las siguientes clases:
    1. `Head`
    2. `Torso`
    3. `Arm`
    4. `Hand`
    5. `Leg`
    6. `Feet`
    7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos."""

class Head:
    def __init__(self):
        self.eyes = 2
        self.mouth = 1
        self.ears = 2
        self.nose = 1
    def __repr__(self):
        return(f'Head(eyes={self.eyes},mouth ={self.mouth},ears = {self.ears},nose ={self.nose})')

class Hand :
    def __init__(self) :
        self.fingers = 5
    def __repr__(self):
        return(f'Hand(fingers={self.fingers})')

class Arm:
    def __init__(self,side):
        self.side = side
        self.hand = Hand()
        self.elbow = 2
        self.shoulder = 2
    def __repr__(self):
        return(f'Arm(side ={self.side} ,hand={self.hand},elbow ={self.elbow},shoulder = {self.elbow})')

class Feet:
    def __init__(self):
        self.fingers = 5
    def __repr__(self):
        return(f'Feet(fingers={self.fingers})')
class Leg:
    def __init__(self,side):
        self.side = side
        self.feet = Feet()
    def __repr__(self):
        return(f'Leg(side ={self.side},feet={self.feet})')

class Torso:
    def __init__(self) :
        self.head = Head() 
        self.right_arm = Arm(side='right')
        self.left_arm = Arm(side='left')
        self.right_leg = Leg(side='right')
        self.left_leg = Leg(side='left')
    
    def __repr__(self):
        return(f'Torso(head={self.head},right_arm ={self.right_arm},left_arm ={self.left_arm},right_leg = {self.right_leg} ,left_leg = {self.left_leg})')
    

class Human:
    def __init__(self):
        self.torso = Torso()
    
    def __repr__(self):
        return(f'Human(torso = {self.torso})')

my_human = Human()
print(my_human)
        