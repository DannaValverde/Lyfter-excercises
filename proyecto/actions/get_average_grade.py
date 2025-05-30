def calculate_student_average(notes):

    if not notes:
        return 0
    return sum(notes.values()) / 4

def avarege_grade(students_list): # receives the list of students
   
    if not students_list:
        print("\nNo students to calculate top 3 average")
        return

    student_averages = []
    for student in students_list:
        name = student.get('name')
        notes = student.get('notes', {})
        average = calculate_student_average(notes) # Use the helper function
        student_averages.append({'name': name, 'average': average})

    valid_averages = []

    for i in student_averages:
        if i['average'] is not None:
             valid_averages.append(i)

    sorted_averages = sorted(valid_averages, key=lambda x: x['average'], reverse=True) #sort from highest to lowest average


    print("\ntop 3 Students with Best Average Grade")
    if not sorted_averages:
        print("no students with averages available for top 3, enter a minimum of 3 students to be able to get the top 3")
        return

    top = sorted_averages[:3]  #get up to the top 3 students
    position = 1

    for student in top:
        name = student['name']
        average = student['average']
        print(str(position) + ". " + name + ": " + str(average))
        position += 1
