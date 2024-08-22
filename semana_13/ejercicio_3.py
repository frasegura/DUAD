"""3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así."""

from datetime import date

class User():
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth


    @property
    def get_age(self):
        age = date.today().year - self.date_of_birth.year
        return age
    

def check_user_age_decorator(func):
    def wrapper(user):
        try:
            if user.get_age > 18:
                print('You can create an account ')
                func(user)
            else:
                raise ValueError('You cannot create an account! Try again')
        except Exception as e:
            print(e)
            main()

    return wrapper

@check_user_age_decorator
def create_user(user_x):
    user_name = input('Please enter your user name: ')
    print(f'User name : {user_name} , age : {user_x.get_age}')

def main():
    user_x = User(date(int(input('year of birth : ')),int(input('month of birth :')),int(input('day of birth : '))))
    create_user(user_x)


if __name__ == '__main__':
    main()





