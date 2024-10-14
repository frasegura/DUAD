import PySimpleGUI as sg

def add_category():
        #category_array = []
        layout_category = [[sg.Text('Please add a category')],
                        [sg.InputText(key='category_name')],
                        [sg.Button('Add Category'), sg.Cancel()]]        
        category_window = sg.Window('Personal Finance Management System', layout_category , finalize=  True)
        while True:
                event,values = category_window.read()
                if event == sg.WIN_CLOSED  or event == 'Cancel':
                        break
                if event == 'Add Category':
                        pass
        category_window.close()
