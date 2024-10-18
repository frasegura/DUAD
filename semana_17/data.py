import json
import os
#import PySimpleGUI as sg

#Escribir el archivo json para guardar los datos:

def write_data_to_json_file(data, file_path = r'semana_17\table_data.json'):
    with open(file_path , 'w') as file :
        json.dump(data, file)

def load_data_from_json_file(file_path = r'semana_17\table_data.json'):
    if not os.path.exists(file_path):
        return None
        
    else:
        with open(file_path,'r') as file:
            data = json.load(file)
        return data