from actions.recoleccion_notes import get_all_notes
import os 

def student_data():
    students = []

    while True:
        name = str(input('Enter student name: '))
        if not name:
            print("The name can't remain empty")
            continue

        section = str(input('Enter student section: '))
        if not section:
            print("The section can't remain empty")
            continue

        print("Enter the student's grades")  # mensaje informativo
        notes = get_all_notes()  # llamar solo una vez

        students.append({
            'name': name,
            'section': section,
            'notes': notes
        })

        while True:
            answer = input('Do you want to add another student? (yes/no): ').strip().lower()
            if answer == 'yes':
                break           # agregar otro estudiante
            if answer == 'no':
                return students
            print('invalid answer. Enter "yes" or "no" ')
