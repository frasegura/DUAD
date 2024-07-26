import csv
import os


#export data to a CSV file
def write_students_in_CSV_file(path,student_info,student_headers):
    with open(path,'w',encoding= 'UTF-8') as file:
        writer = csv.DictWriter(file,fieldnames=student_headers)
        writer.writeheader()
        writer.writerows(student_info)


def read_students_in_csv_file(file_path):
    if not os.path.isfile(file_path):
        raise Exception("There isn't an existing file yet.")
    else:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
