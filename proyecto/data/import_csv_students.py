# data/import_csv_students.py

import csv
import os

def import_data(filename='students_export.csv'):
 
    if not os.path.exists(filename):     #  Check if the file exists
        print("File " , filename, "not found. Please export data first")
        return None

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("File ",filename, "is empty or missing headers")
            return []

        subjects = []
        for header in reader.fieldnames:
            key = header.lower().replace(" ", "_")
            if key not in ('name', 'section'):
                subjects.append(key)

        students_data = []

        for row in reader:
            student = {
                'name':    row.get('name', ''),
                'section': row.get('section', ''),
                'notes':   {}
            }
        
            students_data.append(student)

    print( "data successfully imported from: ", filename)
    return students_data
