def display_Theinput_Data(students_list): 
    
    if not students_list:
        print("\nNo students entered to display.")
        return

    print("\n--- Information for All Entered Students ---")
    for student in students_list:
        print(f"  Name: {student.get('name', 'N/A')}")
        print(f"  Section: {student.get('section', 'N/A')}")
        print("  Grades:")
        notes = student.get('notes', {})
        for subject, note in notes.items():
            print(subject, note)

