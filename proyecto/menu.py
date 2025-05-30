from actions.recoleccion_data import student_data
from actions.see_inputted_data import display_Theinput_Data
from actions.get_average_grade import avarege_grade
from actions.general_average import show_general_average
from data.export_all_data_to_csv import export_Data
from data.import_csv_students import import_data


def show_menu():
    current_students_data = []    #we can modify the global list



    while True:
        print("\n-----------------------------  MENU -------------------------------")
        print("1) Enter student data")
        print("2) View information for all entered students")
        print("3) See the top 3 students with the best average grade")
        print("4) See the average grade of all students")
        print("5) Export all current data to a CSV file")
        print("6) Import data from a previously exported CSV file")
        print("7) Exit")

        option = input("Select the option you want to enter (number): ").strip()

        if option == "1":
            # call student_data to collect new students returns a list of dictionaries for the new students
            new_students = student_data()
            if new_students:
                #dd the newly collected students to our main list of students
                current_students_data.extend(new_students) 
                print(len(new_students), "students added to the current list")

            else:
                print("\nNo new student data was entered")

        elif option == "2":
            # pass the current list of students to the display 
            if current_students_data:
                display_Theinput_Data(current_students_data)
            else:
                print("\nNo student data entered to display\n Please enter students first")
        elif option == "3":
            #pass the current list of students to the function that calculates and displays the top 3
            if current_students_data:
                avarege_grade(current_students_data)
            else:
                print("\nNo student data to calculate top 3 \n Please enter students first.")

        elif option == "4":
            if current_students_data:
                show_general_average(current_students_data)
            else:
                print("\nNo student data to calculate general average \n Please enter students first")

        elif option == "5":
            #pass the current list of students to the export function.
            if current_students_data:
                export_Data(current_students_data)
            else:
                print("\nNo student data to export to CSV. Please enter students first")
        
        elif option == "6":
            # Call the import function returns the imported data
            imported_students = import_data()
            if imported_students is not None:
                if imported_students:
                    current_students_data = imported_students 
                    print(len(current_students_data), "students imported. Current data updated")
                else:
                    print("\nThe imported CSV file is empty or contains no valid data.")
            
        elif option == "7":
            print("Exiting the program..")
            break 

        else:
            print("\nInvalid option. Please select a number from 1 to 7")

