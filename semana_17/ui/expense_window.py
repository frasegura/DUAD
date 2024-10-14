import PySimpleGUI as sg


def check_inputs(new_expense):
        for i in new_expense:
                if i == '':
                    raise ValueError('All fields are mandatory!')

def add_expense():
        try:
            layout_expense =[[sg.Text('EXPENSES')],
                            [sg.Text('Category')],
                            [sg.InputText(key='expense_category')],
                            [sg.Text('Name')],
                            [sg.InputText(key='expense_name')],
                            [sg.Text('Amount ($)')],
                            [sg.InputText(key='expense_amount')],
                            [sg.Button('Add'),sg.Cancel()]]
            
            expense_window = sg.Window('Personal Finance Management System',layout_expense, finalize=True)
            while True:
                    event, values = expense_window.read()
                    if event == sg.WIN_CLOSED or event == 'Cancel':
                            break
                    elif event == 'Add':
                        new_expense = [values['expense_category'],values['expense_name'], values['expense_amount']]
                        check_inputs(new_expense)
                        new_expense.insert(2,'expense')
                        sg.popup('Information submitted !')
                        expense_window.close()
                        return new_expense
        except Exception as e:
            sg.popup(f'Invalid information :{e}')
        finally:
            expense_window.close()