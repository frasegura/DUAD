#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class Character():
    def __init__(self,name,sword,magic):
        self.name = name
        self.sword = sword
        self.magic = magic

    def attributes(self):
        print(self.name)
        print(f'* Sword power : {self.sword}')
        print(f'* Magic power : {self.magic}')
        
    
class Warrior(Character):

    def power_up_sword_attack(self):
        option = int(input('Please select the sword you want to use : (1)Excalibur , damage : 5.   (2) Sould Edge , damage 6.   :'))
        if option == 1:
            self.sword = 5
            print('Excalibur sword selected')
            
        elif option == 2 : 
            self.sword = 6
            print('Soul Edge sword selected')
        else:
            print('Invalid option')

        print(self.sword)

        
    def attributes(self):
        super().attributes()
        
class Wizard(Character):

    def power_up_magic_attack(self):
        option =int(input('Please selected your spell : (1) Shadow garden ,damage : 7.    (2)Unlimited void ,damage : 10.   : '))
        if option == 1:
            self.magic = 7
        elif option == 2:
            self.magic = 10
        
        print(self.magic)

    def attributes(self):
        super().attributes()


class WarriorWizard(Warrior,Wizard):
    
    def attributes(self):
        super().attributes()
        print(f'* Special attack : {self.special_attack()}')

    def special_attack(self):
        damage = self.sword * self.magic
        return damage
        

def powering_up(special_character):
    option = input('Do you want to add a power up for your character: (yes/no):  ')

    if option == 'yes':
        special_character.power_up_sword_attack()
        special_character.power_up_magic_attack()
        print('Power up added !')
        special_character.attributes()
    elif option == 'no':
        print('No power up added.')
        special_character.attributes()


def main():
    
    characters_name = input("Please enter su character's name : ")
    input(f'Welcome {characters_name}')
    print('(1)Warrior')
    print('(2)Wizard')
    print('(3)Warrior-Wizard')
    option = int(input(" Please select your character's class : "))

    if option == 1:
        warrior = Warrior(characters_name,3,0)       
        warrior.attributes()
    elif option == 2:
        wizard = Wizard(characters_name,0,4)
        wizard.attributes()
    elif option == 3:
        special_character = WarriorWizard(characters_name,2,1)
        special_character.attributes()
        powering_up(special_character)
    else :
        print('Invalid option')


if __name__ == '__main__':
    main()

