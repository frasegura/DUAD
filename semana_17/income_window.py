import PySimpleGUI as sg

def check_inputs(new_income):
    for i in new_income:
        if i == '':
            raise ValueError('All fields are mandatory')
        
    if not new_income[1].isalpha():
            raise ValueError('Only letters are allowed in the income name field')
        
    if not new_income[2].isdigit():
            raise ValueError('Only numbers are allowed in the amount field')


def add_income(categories):

    layout_income = [[sg.Text('INCOMES')],
                    [sg.Text('Category')],
                    [sg.Combo(key='income_category',values=categories,auto_size_text =True)],
                    [sg.Text('Name')],
                    [sg.InputText(key='income_name')],
                    [sg.Text('Amount ($)')],
                    [sg.InputText(key='income_amount')],
                    [sg.Input(key='income',visible=False)],
                    [ sg.Button('Add'), sg.Cancel()]]       
    income_window = sg.Window('Personal Finance Management System',layout_income,finalize= True)
    while True:
            
            try: 
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
            except Exception as e:
                sg.popup(f'Invalid information :{e}')
                    
    income_window.close()
    
