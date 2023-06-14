from modules.person import Student, Admin
from modules.course import Course

class Display:
    def __init__(self):
        pass



    def display_students_and_courses(self, students, courses):
        """
        Displays the list of students and courses.

        :param students: A list of Student objects.
        :param courses: A list of Course objects.
        """
        print("Students:")
        for student in students:
            print(f"{student.name} ({student.id_number})")
        print("\nCourses:")
        for course in courses:
            print(f"{course.course_code}: {course.course_name}")


    def display_items(self, items):
        """
        Displays the list of filtered students.

        :param filtered_students: A list of filtered Student objects.
        """
        for item in items:
            if isinstance(item, Admin):
                print(f"Admin: {item.name} ({item.id_number})")

            if isinstance(item, Student):
                print(f"Student: {item.name} ({item.id_number})")

            if isinstance(item, Course):
                print(f"Professor: {item.course_code} ({item.course_name})")



    def display_sorted_courses(self, courses):
        """
        Displays the list of sorted courses.

        :param courses: A list of sorted Course objects.
        """
        print("Courses:")
        for course in courses:
            print(f"{course.course_code}: {course.course_name}")


    def view_my_enrollments(self, user, courses, students_courses):
        """
        Displays the courses a student is enrolled in.
        :param user: A Student object.
        :param courses: A list of Course objects.
        :param students_courses: A dictionary with student ID as the key and a list of course codes as the value.
        """
        print("My Enrollments:")
        if user.id_number in students_courses:
            enrolled_course_codes = students_courses[user.id_number]
            for course_code in enrolled_course_codes:
                course = next((c for c in courses if c.course_code == course_code), None)
                if course:
                    print(f"{course.course_code} - {course.course_name}")
        else:
            print("You are not enrolled in any courses.")

    def view_available_courses(self, courses):
        """
        Displays the list of available courses.
        :param courses: A list of Course objects.
        :param professors_courses: A dictionary containing professors and their courses.
        :param professors: A list of Professor objects.
        """
        print("Available Courses:")
        for course in courses:
            print(f"{course.course_code}: {course.course_name}")

