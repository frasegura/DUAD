
import PySimpleGUI as sg
import expense_window
import category_window
import income_window
from  data import load_data_from_json_file,write_data_to_json_file

#1. Definir temas de color disponibles
sg.theme('DarkTeal9')

class ExistingCategory(Exception):
        pass

class EmptyCategoryList(Exception):
        pass

def check_categories(categories):
        try:
                if categories == []:
                        raise EmptyCategoryList('You need to enter categories to enter information')  
                return True       
        except EmptyCategoryList as e:
                sg.popup(e)
                return False
        
def category_submission(categories):
        try:
                new_category = category_window.select_type_category()
                if new_category  in categories:      
                        raise ExistingCategory('The category entered already exists')
                        #return categories
                if new_category is None:
                        return categories
                categories.append(new_category)
                sg.popup('Category created !')
        except ExistingCategory as e:
                sg.popup(e)
        return categories

def income_submission(table_data, main_window,categories):
        new_income = income_window.add_income(categories)
        if new_income:
                table_data.append(new_income)
                main_window['Table'].update(values = table_data)  

def expense_submission(table_data, main_window,categories):
        new_expense = expense_window.add_expense(categories)
        if new_expense:
                table_data.append(new_expense)
                main_window['Table'].update(values = table_data)

def show_main_window():
        table_headings = ['Category','Name','Type','Amount']
        table_data, categories, incomes_categories , expenses_categories = [],[],[],[]

        info = load_data_from_json_file()

        table_data = info.get('table_data',[])
        categories = info.get('categories',[])
        incomes_categories = info.get('incomes_categories',[])
        expenses_categories = info.get('expenses_categories',[])

        

        try:    
                #2.Definir elementos del layout
                main_window_layout = [[sg.Text('Welcome to you finance assistent')],
                        [sg.Table(values= table_data ,headings= table_headings,justification='right',key ='Table',auto_size_columns= True)],
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
                                categories = category_submission(categories)
                                for i in categories:
                                        if '-I' in i:
                                                if i not in incomes_categories:
                                                        incomes_categories.append(i)
                                                
                                        elif '-E' in i:
                                                if i not in expenses_categories:
                                                        expenses_categories.append(i)
                                                
                                write_data_to_json_file({
                                        'table_data' : table_data,
                                        'categories' : categories,
                                        'income_categories' : incomes_categories,
                                        'expenses_categories' : expenses_categories
                                })

                        elif event == 'Add Income':
                                if check_categories(incomes_categories):
                                        income_submission(table_data, main_window,incomes_categories)

                                write_data_to_json_file({
                                        'table_data' : table_data,
                                        'categories' : categories,
                                        'income_categories' : incomes_categories,
                                        'expenses_categories' : expenses_categories
                                })

                        elif event == 'Add Expense':
                                if check_categories(expenses_categories):
                                        expense_submission(table_data, main_window, expenses_categories)

                                write_data_to_json_file({
                                        'table_data' : table_data,
                                        'categories' : categories,
                                        'income_categories' : incomes_categories,
                                        'expenses_categories' : expenses_categories
                                })

                #5.Cerrar la ventana
                main_window.close()
        except Exception as e:
                sg.popup(f'An error has ocurred : {e}')
                print(f'An error has ocurred : {e}')
                show_main_window()
                

if __name__ == '__main__':
        show_main_window()


        
