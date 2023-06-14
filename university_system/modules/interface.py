from modules.utils import Utils
from modules.data_saver import Saver
from modules.add_object import AddObject
from modules.display import Display
from modules.data_loader import Loader

from modules.person import Student, Admin

class Interface:
    def __init__(self):
        self.loader = Loader()
        self.utils = Utils()
        self.saver = Saver()
        self.adder = AddObject()
        self.displayer = Display()

    def show_interface(self):
        """
        The main function of the University Management System program.
        """

        STUDENTS_FILE = 'data/students.csv'
        ADMINS_FILE = 'data/admins.csv'
        COURSES_FILE = 'data/courses.csv'
        STUDENTS_COURSES_FILE = 'data/students_courses.csv'

        students = self.loader.load_students(STUDENTS_FILE)
        admins = self.loader.load_admins(ADMINS_FILE)
        courses = self.loader.load_courses(COURSES_FILE)
        students_courses_grades = self.loader.load_students_courses(STUDENTS_COURSES_FILE)

        user_id = input("Enter your ID number, 0 to exit: ")
        user = None


        if user_id == '0':
            return

        if students != []:
            for student in students:
                if student.id_number == user_id:
                    user = student
                    print("Student found.")

        if admins != []:
            for admin in admins:
                if admin.id_number == user_id:
                    user = admin
                    print("Admin found.")

        if not user:
            print("Invalid ID.")
            return
        
        while True:
            if isinstance(user, Admin):
                while True:
                    self.display_admin_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        self.adder.add_student(students)
                        self.saver.save_students(STUDENTS_FILE, students)
                    elif choice == '2':
                        self.adder.add_course(courses)
                        self.saver.save_courses(COURSES_FILE, courses)
                    elif choice == '3':
                        self.adder.add_admin(admins)
                        self.saver.save_admins(ADMINS_FILE, admins)
                    elif choice == '4':
                        self.displayer.display_items(students)
                    elif choice == '5':
                        self.displayer.display_items(admins)
                    elif choice == '6':
                        self.displayer.display_items(students)
                        self.displayer.display_items(admins)
                    elif choice == '7':
                        self.displayer.display_sorted_courses(courses)
                    elif choice == '8':
                        filtered_students = self.utils.filter_students_by_course(students, students_courses_grades)
                        self.displayer.display_items(filtered_students)
                    elif choice == '9':
                        sorted_students = self.utils.sort_students_by_name(students)
                        self.displayer.display_items(sorted_students)
                    elif choice == '10':
                        sorted_courses = self.utils.sort_courses_by_name(courses)
                        self.displayer.display_items(sorted_courses)      
                    elif choice == '11':
                        self.adder.enroll_student_by_id_and_course_code(students, courses, students_courses_grades, force=True)
                        self.saver.save_students_courses(STUDENTS_COURSES_FILE, students_courses_grades)

                    elif choice == '0':
                        self.saver.save_admins(ADMINS_FILE, admins)
                        self.saver.save_students(STUDENTS_FILE, students)
                        self.saver.save_courses(COURSES_FILE, courses)
                        self.saver.save_students_courses(STUDENTS_COURSES_FILE, students_courses_grades)
                        return

                    else:
                        print("Invalid choice. Try again.")

            elif isinstance(user, Student):
                while True:
                    self.display_student_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        self.displayer.view_my_enrollments(user, courses, students_courses_grades)
                    elif choice == '2':
                        self.displayer.view_available_courses(courses)
                    elif choice == '3':
                        self.adder.enroll_student_by_id_and_course_code(students, courses, students_courses_grades, False)

                    elif choice == '0':
                        self.saver.save_admins(ADMINS_FILE, admins)
                        self.saver.save_students(STUDENTS_FILE, students)
                        self.saver.save_courses(COURSES_FILE, courses)
                        self.saver.save_students_courses(STUDENTS_COURSES_FILE, students_courses_grades)
                        return

                    else:
                        print("Invalid choice. Try again.")


    def display_admin_menu(self):
        """
        Displays the admin menu.
        """
        print("Admin Menu")
        print("1. Add student")
        print("2. Add course")
        print("3. Add admin")
        print("4. Display students")
        print("5. Display admins")
        print("6. Display all people")
        print("7. Display courses")
        print("8. Filter students by course")
        print("9. Sort students by name")
        print("10. Sort courses by name")
        print("11. Enroll student in a course (override max courses)")

        print("0. Exit")


    def display_student_menu(self):
        """
        Displays the student menu.
        """
        print("Student Menu")
        print("1. View my enrollments")
        print("2. View available courses")
        print("3. Enroll in a course")

        print("0. Exit")
