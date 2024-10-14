
import PySimpleGUI as sg
import expense_window
import category_window
import income_window

#1. Definir temas de color disponibles
sg.theme('DarkTeal9')

def income_submission(table_data, main_window):
        new_income = income_window.add_income()
        if new_income:
                table_data.append(new_income)
                main_window['Table'].update(values = table_data)  

def expense_submission(table_data, main_window):
        new_expense =expense_window.add_expense()
        if new_expense:
                table_data.append(new_expense)
                main_window['Table'].update(values = table_data)

def show_main_window():

        
        table_headings = ['Category','Name','Type','Amount']
        table_data = []

        #2.Definir elementos del layout
        main_window_layout = [[sg.Text('Welcome to you finance assistent')],
                [sg.Table(values= table_data ,headings= table_headings,max_col_width=35,justification='right',key ='Table', row_height=35)],
                [sg.Push() ,sg.Button('Add category'), sg.Button('Add Income'),sg.Button('Add Expense'),sg.Push()]
                ]
        #3.Configurar la ventana
        main_window = sg.Window('Personal Finance Management System', main_window_layout, finalize= True)


        #4.Mostrar las demas ventanas y leer eventos
        while True:
                event, values = main_window.read()
                if event == sg.WIN_CLOSED:
                        break
                elif event == 'Add category':
                        category_window.add_category()
                elif event == 'Add Income':
                        income_submission(table_data, main_window)
                elif event == 'Add Expense':
                        expense_submission(table_data, main_window)


        #5.Cerrar la ventana
        main_window.close()

if __name__ == '__main__':
        show_main_window()

