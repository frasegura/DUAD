import csv

#export data to a CSV file
def write_students_in_CSV_file(path,student_info,student_headers):
    with open(path,'w',encoding= 'UTF-8') as file:
        writer = csv.DictWriter(file,fieldnames=student_headers)
        writer.writeheader()
        writer.writerows(student_info)