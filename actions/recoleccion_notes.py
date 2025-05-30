def get_all_notes():
  
    subjects = ["Spanish", "English", "Social Studies", "Science"]
    notes = {}

    for subject in subjects:
        while True:
            try:
                note = int(input(f"enter the grade for {subject} : "))
                if 0 <= note <= 100: # Validation for range 0 to 100
                    key = subject.lower().replace(" ", "_")
                    notes[key] = note
                    break
                else:
                    print("the grade must be between 0 and 100 \n Please enter a valid grade")
            except ValueError:
                print("invalid value please enter a valid number")
    return notes
