from modules.utils import Utils
from modules.course import Course, Enrollment
from modules.person import Student, Admin
from modules.data_loader import Loader

class AddObject:
    def __init__(self):
        self.utils = Utils()
        self.loader = Loader()

    def add_admin(self, admins):
        """
        Adds a new admin to the list of admins.

        :param admins: A list of Admin objects.
        """
        try:
            name = input("Enter admin name: ")
            email = input("Enter admin's email: ")
            id_number = self.utils.generate_unique_id(Admin)
            admins.append(Admin(name, id_number, email))
        except Exception as e:
            print(f"Error adding admin: {e}")

    def add_student(self, students):
        """
        Adds a new student to the list of students.
        
        :param students: A list of Student objects.
        """
        try:
            name = input("Enter student name: ")
            standing = input("Enter student's standing: ")
            id_number = self.utils.generate_unique_id(Student)
            students.append(Student(name, id_number, standing))
        except Exception as e:
            print(f"Error adding student: {e}")

    def add_course(self, courses):
        """
        Adds a new course to the list of courses.
        
        :param courses: A list of Course objects.
        """
        try:
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            courses.append(Course(course_code, course_name))
        except Exception as e:
            print(f"Error adding course: {e}")


    def enroll_student_by_id_and_course_code(
            self, students, courses, students_courses, force=False):
        """
        Enrolls a student in a course by student ID and course code.
        
        :param students: A list of Student objects.
        :param courses: A list of Course objects.
        :param students_courses: A dictionary containing enrolled students as keys and
                                lists of their enrolled course codes as values.
        :param force: If True, overrides the maximum allowed courses (5).
        """
        student_id = input("Enter student ID number: ")
        course_code = input("Enter course code: ")

        # Find the student with the given student_id
        student = next((s for s in students if s.id_number == student_id), None)
        if not student:
            print("Student not found.")
            return
        course = next((c for c in courses if c.course_code == course_code), None)

        count = 0
        for student_id_key, courses_list in students_courses.items():
            if student_id_key == student_id:
                count = len(courses_list)

        if student and course:
            if force or count < 5:
                if students_courses is not None:
                    if student_id not in students_courses:
                        students_courses[student_id] = []
                    students_courses[student_id].append(course_code)
                print("Student successfully enrolled.")
            else:
                print("Student is already enrolled\
                        in the maximum allowed courses (5).")
        else:
            print("Invalid student ID or course code.")




    def enroll_student(self, student, course, students_courses_grades):
        """
        Enrolls a student in a course and initializes the student's grade as "N/A".
        
        :param student: A Student object.
        :param course: A Course object.
        :param students_courses_grades: A dictionary containing enrolled students as keys
                                         and dictionaries of their enrolled course codes
                                         and corresponding grades as values.
        """
        enrollment = Enrollment(student, course)
        if enrollment.student.id_number not in students_courses_grades:
            students_courses_grades[enrollment.student.id_number] = {}
            students_courses_grades[enrollment.student.id_number][enrollment.course.course_code] = "N/A"
