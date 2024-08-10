"""1. Cree una clase de `BankAccount` que:
    1. Tenga un atributo de `balance`.
    2. Tenga un método para ingresar dinero.
    3. Tengo un método para retirar dinero.
    
    Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
    1. Tenga un atributo de `min_balance`.
    2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`."""

class BankAccount():
    def __init__(self,balance):
        self.balance = balance

    def ingresar_dinero(self,amount):
        self.balance = self.balance + amount
        return self.balance
        
    def retirar_dinero(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def account_balance(self):
        print(f'You have : $ {self.balance}')

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
        self.min_balance = 500

    def retirar_dinero(self, amount):
        if self.balance <= self.min_balance:
            print('The require amount cannot be withdrawn due to insufficient balance on the account')
        elif self.balance <= amount:
            print('The required amount cannot be withdrawn because it exceeds the actual balance in the account.')


        else:
            residual_value = self.balance - amount
            if residual_value <= self.min_balance:
                test_value = self.balance - residual_value
                if test_value >= self.min_balance:
                    residual_value = self.balance - self.min_balance
                    print(f' From : {amount } only : {residual_value} can be withdrawn because your account balance is :{self.balance}')
                    self.balance = self.balance - residual_value
                else:
                    print(f'From : {amount } only : {residual_value} can be withdrawn because your account balance is :{self.balance}')
                    self.balance = self.balance - residual_value
                
            else:
                self.balance = self.balance - amount

def show_menu():
    my_account = SavingsAccount(500)
    proceed =  True
    while proceed :
        try:
            print('(1)Make a deposit')
            print('(2)Whitdrawn')
            print('(3)Check account')
            option = int(input('Please enter the option :'))
            
            if option == 1:
                my_account.ingresar_dinero(int(input('Please enter the amount of the deposit: ')))
            elif option ==2 :
                my_account.retirar_dinero(int(input('Please enter the amount to be withdrawn: ')))
            elif option == 3:
                my_account.account_balance()
            else:
                raise ValueError('Opcion invalida')
            proceed = input('Do you want to continue in the menu?(yes/no) : ') == 'yes'
        except Exception as e:
            print(f'Se ha producido un error : {e}')
        

def main():  
    print(f'Welcome : {input('Ingrese su nombre :')}')
    show_menu()


if __name__ == '__main__':
    main()
