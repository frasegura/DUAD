
import PySimpleGUI as sg

#1. Definir temas de color disponibles
sg.theme('DarkTeal9')

def main_window():

        table_data = [['wheel', 'car','expense','$100']]
        table_headings = ['Name','Category','Type','Amount']

        #2.Definir elementos del layout
        main_window_layout = [[sg.Text('Welcome to you finance assistent')],
                [sg.Table(values= table_data ,headings= table_headings,max_col_width=35,justification='right',key ='Table', row_height=35)],
                [sg.Push() ,sg.Button('Add category'), sg.Button('Add Income'),sg.Button('Add Expense'),sg.Push()] ,
                ]



        #3.Configurar la ventana
        main_window = sg.Window('Personal Finance Management System', main_window_layout, finalize= True)


        #4.Mostrar las demas ventanas y leer eventos
        while True:
                event, values = main_window.read()
                if event == sg.WIN_CLOSED:
                        break
                elif event == 'Add category':
                        add_category()
                elif event == 'Add Income':
                        add_income()
                elif event == 'Add Expense':
                        add_expense()

        #5.Cerrar la ventana
        main_window.close()

def add_category():
        layout_category = [[sg.Text('Please add a category')],
                        [sg.InputText()],
                        [sg.Button('Add Category'), sg.Cancel()]]
        
        category_window = sg.Window('Personal Finance Management System', layout_category , finalize=  True)
        while True:
                event,values = category_window.read()
                if event == sg.WIN_CLOSED :
                        break
        category_window.close()

def add_income():
        layout_income = [[sg.Text('INCOMES')],
                        [sg.Text('Name')],
                        [sg.InputText()],
                        [sg.Text('Amount')],
                        [sg.InputText()],
                        [sg.Text('Category')],
                        [sg.InputText()],
                        [ sg.Button('Add'), sg.Cancel()]]
        
        income_window = sg.Window('Personal Finance Management System',layout_income,finalize= True)
        while True:
                event, values = income_window.read()
                if event == sg.WIN_CLOSED:
                        break
        income_window.close()

def add_expense():
        layout_expense =[[sg.Text('EXPENSES')],
                        [sg.Text('Name')],
                        [sg.InputText()],
                        [sg.Text('Amount')],
                        [sg.InputText()],
                        [sg.Text('Category')],
                        [sg.InputText()],
                        [sg.Button('Add'),sg.Cancel()]]
        
        expense_window = sg.Window('Personal Finance Management System',layout_expense, finalize=True)
        while True:
                event, values = expense_window.read()
                if event == sg.WIN_CLOSED:
                        break
        expense_window.close()


if __name__ == '__main__':
        main_window()

