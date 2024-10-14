import PySimpleGUI as sg

def check_inputs(new_income):
    for i in new_income:
        if i == '':
            raise ValueError('All fields are mandatory')

def add_income():
        try:
            layout_income = [[sg.Text('INCOMES')],
                            [sg.Text('Category')],
                            [sg.InputText(key='income_category')],
                            [sg.Text('Name')],
                            [sg.InputText(key='income_name')],
                            [sg.Text('Amount ($)')],
                            [sg.InputText(key='income_amount')],
                            [sg.Input(key='income',visible=False)],
                            [ sg.Button('Add'), sg.Cancel()]]       
            income_window = sg.Window('Personal Finance Management System',layout_income,finalize= True)
            while True:
                    event, values = income_window.read()
                    if event == sg.WIN_CLOSED or event == 'Cancel':
                            break
                    elif event == 'Add':
                            new_income = [values['income_category'],values['income_name'],values['income_amount']]
                            check_inputs(new_income)
                            new_income.insert(2,'income')
                            sg.popup('Information submitted !')
                            income_window.close()
                            return new_income
                        

            #income_window.close()
            #return None # si devuelve none va tirar un pop up
        except Exception as e:
            sg.popup(f'Invalid information :{e}')
        finally:
            income_window.close()
    
