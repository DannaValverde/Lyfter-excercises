import csv

def export_Data(students_list, filename='students_export.csv'):  
    
    #Exports the list of student data to a CSV file.
    if not students_list:
        print("\nno student data to export to CSV")
        return

    headers = ['name', 'section']
    all_subjects = set()

    for student in students_list:
        if 'notes' in student:
            notes = student['notes']
        if type(notes) == dict:
            for subject in notes:
                all_subjects.add(subject)


    sorted_subjects = sorted(all_subjects) 
    headers.extend(sorted_subjects)

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for student in students_list:
            row = {
                'name': student.get('name', ''),
                'section': student.get('section', '')
            }
            notes = student.get('notes', {}) #add grades to the row dictionary
            for subject in sorted_subjects:
                row[subject] = notes.get(subject, '')  
            writer.writerow(row)

    print("\nstudent data successfully exported to: ",filename)
