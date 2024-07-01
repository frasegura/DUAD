from actions import create_student,show_all_students,get_top_three_students,get_average_grade_all_students
from data import write_students_in_CSV_file

def check_option(option):
    if not 1 <= option <= 6:
        raise ValueError('Invalid option, you have to select an option within the range from 1 to 6')


def check_empty_list(student_info): #ver en preguntas notion
    if len(student_info) ==  0:
        raise ValueError('The list is empty')


def show_menu():
    option = 0
    proceed = True
    student = dict()
    amount_students= 0
    student_info = list()
    file_path = r'semana_10\estudiantes.csv'
    student_headers = ('full_name', 'student_section','spanish_grade','english_grade','social_studies_grade','science_grade','average_grade')

    while proceed :

        try:
            print('1)Add student.')
            print('2)Display information for all the added students.')
            print('3)Display the top 3 students with the best grades.')
            print('4)Show the average grade of all students.')
            print('5)Export the data to a CSV file.')
            print('6)Import data from a CSV file.')
            option = int(input('Please select an option:'))
            check_option(option)

            if(option==1):
                student_info =create_student(student,amount_students)
            elif(option == 2):
                check_empty_list(student_info)
                show_all_students(student_info)
            elif(option == 3):
                check_empty_list(student_info)
                get_top_three_students(student_info)
            elif(option == 4):
                check_empty_list(student_info)
                get_average_grade_all_students(student_info)
            elif(option == 5):
                check_empty_list(student_info)
                write_students_in_CSV_file(file_path,student_info,student_headers)
            elif(option == 6):
                print('import data from CSV file')
            proceed = input('Do you want to continue in the menu?(yes/no) : ') == 'yes'
        except Exception as e:
            print(f'An error has ocurred : {e}')
            


