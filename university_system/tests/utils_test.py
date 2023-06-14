import unittest
from unittest.mock import patch
from modules.person import Student
from modules.course import Course
from modules.utils import Utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.utils = Utils()

    def test_float_to_letter_grade(self):
        self.assertEqual(self.utils.float_to_letter_grade(95), 'A')
        self.assertEqual(self.utils.float_to_letter_grade(85), 'B')
        self.assertEqual(self.utils.float_to_letter_grade(75), 'C')
        self.assertEqual(self.utils.float_to_letter_grade(65), 'D')
        self.assertEqual(self.utils.float_to_letter_grade(55), 'F')

    def test_sort_students_by_name(self):
        student1 = Student(name='Alex', id_number='1234567890', standing='Senior')
        student2 = Student(name='Zack', id_number='2345678901', standing='Junior')
        student3 = Student(name='Bob', id_number='3456789012', standing='Sophomore')
        students = [student1, student2, student3]
        sorted_students = self.utils.sort_students_by_name(students)
        self.assertEqual(sorted_students, [student1, student3, student2])

    def test_sort_courses_by_name(self):
        course1 = Course(course_code='CSC101', course_name='Introduction to Computer Science')
        course2 = Course(course_code='MTH101', course_name='Calculus')
        course3 = Course(course_code='ENG201', course_name='English Literature')
        courses = [course1, course2, course3]
        sorted_courses = self.utils.sort_courses_by_name(courses)
        self.assertEqual(sorted_courses, [course2, course3, course1])

    def test_generate_unique_id(self):
        student = Student("name", "0", "freshman")
        student.id_number = self.utils.generate_unique_id(Student)
        student_id = student.id_number

        self.assertIsInstance(student_id, str)
        self.assertEqual(len(student_id), 10)

if __name__ == '__main__':
    unittest.main()
