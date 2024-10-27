import PySimpleGUI as sg

def check_input(my_categ):
        if my_categ == '':
                raise ValueError('All fields are mandatory')
        
        if not my_categ[0].isalpha():
                raise ValueError('Only letters are allowed in the category name field')
        


def select_type_category():
        layout_type_category = [[sg.Text('Please select the category type you want to add:')],
                                [sg.Button('Add Income Category'), sg.Button('Add Expense Category'),sg.Cancel()]]

        type_of_category_window = sg.Window('Personal Finance Management System', layout_type_category, finalize= True)
        while True:
                event,values =  type_of_category_window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel':
                        type_of_category_window.close()
                        return None
                elif event == 'Add Income Category':
                        income_category = add_category()
                        if income_category is None:
                                continue
                        type_of_category_window.close()
                        return income_category + '-I'
                elif event == 'Add Expense Category':
                        expense_category = add_category()
                        if expense_category is None:
                                continue
                        type_of_category_window.close()
                        return expense_category + '-E'

def add_category():
        layout_category = [[sg.Text('Please add a category')],
                [sg.InputText(key='category_name')],
                [sg.Button('Add Category'), sg.Cancel()]]        
        category_window = sg.Window('Personal Finance Management System', layout_category , finalize=  True)
        while True:
                try:
                        event,values = category_window.read()
                        if event == sg.WIN_CLOSED  or event == 'Cancel':
                                category_window.close()
                                return None
                        if event == 'Add Category':
                                new_category = values['category_name']
                                check_input(new_category)
                                category_window.close()
                                return new_category
                except Exception as e:
                        sg.popup(f'Invalid information : {e}')
