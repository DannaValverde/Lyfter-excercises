from actions.get_average_grade import calculate_student_average

def show_general_average(students_list): #receives the list of students

    if not students_list:
        print("No students to calculate the general average.")
        return

    all_student_averages = []
    for student in students_list:
        notes = student.get('notes', {})
        if notes: 
            all_student_averages.append(calculate_student_average(notes))
    
    if all_student_averages:
        general_average = sum(all_student_averages) / 4
        print("\noverall Average Grade for all Students: ", str(general_average))

    else:
        print("\ncould not calculate general averages, either no students or no grades recorded")