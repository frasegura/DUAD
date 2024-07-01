from actions import create_student

def check_option(option):
    if not 1 <= option <= 6:
        raise ValueError('Invalid option, you have to select an option within the range from 1 to 6')

def show_menu():
    option = 0
    proceed = True
    student = dict()
    amount_students= 0

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
                create_student(student,amount_students)
            elif(option == 2):
                print('show  the information of all students')
            elif(option == 3):
                print('show the top three students with the best average grade')
            elif(option == 4):
                print('show the average grade of all students.')
            elif(option == 5):
                print('export data to a CSV file')
            elif(option == 6):
                print('import data from CSV file')
            proceed = input('Do you want to continue (yes/no) : ') == 'yes'
        except Exception as e:
            print(f'An error has ocurred : {e}')
            


