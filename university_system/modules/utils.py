import random

class Utils:
    def __init__(self):
        pass

    def sort_students_by_name(self, students):
        """
        Sorts students by name.
        :param students: A list of Student objects.
        :return: A list of sorted Student objects.
        """
        return sorted(students, key=lambda s: s.name)


    def filter_students_by_course(self, students, students_courses_grades):
        """
        Filters students by the course they are enrolled in.
        :param students: A list of Student objects.
        :param students_courses_grades: A dictionary with student_id as keys and dictionaries of course_code and grade as values.
        :return: A list of filtered Student objects.
        """

        course_code = input("Enter course code: ")
        enrolled_student_ids = [student_id for student_id, courses in students_courses_grades.items() if course_code in courses]
        filtered_students = [student for student in students if student.id_number in enrolled_student_ids]
        return filtered_students


    def sort_courses_by_name(self, courses):
        """
        Sorts courses by name.
        :param courses: A list of Course objects.
        :return: A list of sorted Course objects.
        """
        return sorted(courses, key=lambda c: c.course_name)

    def generate_unique_id(self, cls):
        """
        Generate a unique 10-digit ID number for a Person.
        :return: A unique 10-digit string.
        """
        while True:
            id_number = str(random.randint(1000000000, 9999999999))
            if not any(p.id_number == id_number for p in cls._instances):
                return id_number

