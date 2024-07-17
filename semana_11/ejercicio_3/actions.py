
class Student:
    def __init__(self,name,section,spanish_grade,english_grade,social_studies_grade,science_grade,average_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_studies_grade = social_studies_grade
        self.science_grade = science_grade
        self.average_grade = average_grade

    def __repr__(self) :
        return (f'Student(name={self.name}, section={self.section}, spanish_grade={self.spanish_grade}, '
                f'english_grade={self.english_grade}, social_studies_grade={self.social_studies_grade}, '
                f'science_grade={self.science_grade}, average_grade={self.average_grade})')
    
class StudentsGroup:
    def __init__(self) :
        self.students_list = []

    def add_students(self):
        name = input("Please enter the student's name : ")
        check_empty_field(name)
        check_words(name)

        section = input('Please enter the section of the student:')
        check_empty_field(section)

        spanish_grade = input('Please enter the spanish grade:')
        check_empty_field(spanish_grade)
        check_numbers(spanish_grade)
        check_grades(float(spanish_grade))

        english_grade = input('Please enter the english grade:')
        check_empty_field(english_grade)
        check_numbers(english_grade)
        check_grades(float(english_grade))

        social_studies_grade = input('Please enter the social studies grade:')
        check_empty_field(social_studies_grade)
        check_numbers(social_studies_grade)
        check_grades(float(social_studies_grade))

        science_grade =input('Please enter the science grade:')
        check_empty_field(science_grade)
        check_numbers(science_grade)
        check_grades(float(science_grade))

        average_grade_student = get_average(spanish_grade,english_grade,social_studies_grade,science_grade)
        student = Student(name,section,spanish_grade,english_grade,social_studies_grade,science_grade,average_grade_student)
        self.students_list.append(student) 
    
    

def check_words(name):
    if all( word.isalpha() for word  in name.split() ):
        print('Name captured correctly!')
    else:
        raise ValueError('Invalid information! you can only enter words.')


def check_numbers(number):
    try:
        float(number)
    except Exception as e:
        raise ValueError(' Invalid information! you can only enter numbers.')
    
        
def check_grades(grade):
    if not 0 <= grade <= 100:
        raise ValueError('The grade entered is invalid, it should be in a range between 0 and 100.')
    

def check_empty_field(field):
    if not field:
        raise ValueError('You must enter a value; it cannot be left blank!')


def get_average(spanish_grade,english_grade,social_studies_grade,science_grade):
    sum_grades = float(spanish_grade)+float(english_grade)+float(social_studies_grade)+float(science_grade)
    average_grade = sum_grades/4
    return average_grade

def create_student(amount_students):
    continue_entering_students = True
    #students_list =[]
    group = StudentsGroup()
    while continue_entering_students:
        try:
            group.add_students()
            amount_students +=1
            continue_entering_students = input('Would you like to add other student? (yes/no):') == 'yes'
        except Exception as e:
            print(f'An error occurred while capturing the student s info : {e}')
    return(group.students_list)


def show_all_students(student_info):
    print(student_info)

    
def get_top_three_students(student_info):
    sorted_students = sorted(student_info, key=lambda student :student.average_grade, reverse=True)
    for student in sorted_students[:3]:
        print(student.name)


#show the average grade of all students
def get_average_grade_all_students(student_info):
    sum_general_grade = 0
    average_general_grade = 0
    for student in student_info:
        sum_general_grade += student.average_grade
    average_general_grade = sum_general_grade/len(student_info)
    print(f'The average grade of all students is : {"{:.2f}".format(average_general_grade)}')
        



