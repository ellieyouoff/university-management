import io
import sys
import unittest
from modules.person import Student, Admin
from modules.course import Course
from modules.display import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display()

    def test_display_students_and_courses(self):
        fake_output = io.StringIO()
        sys.stdout = fake_output

        student1 = Student(name="John Doe", id_number="1111111111")
        student2 = Student(name="Jane Smith", id_number="2222222222")
        course1 = Course(course_code="COS101", course_name="Intro to Computer Science")
        course2 = Course(course_code="MTH101", course_name="Calculus I")

        self.display.display_students_and_courses([student1, student2], [course1, course2])
        expected_output = "Students:\nJohn Doe (1111111111)\nJane Smith (2222222222)\n\nCourses:\nCOS101: Intro to Computer Science\nMTH101: Calculus I\n"

        self.assertEqual(fake_output.getvalue(), expected_output)

        sys.stdout = sys.__stdout__

    def test_display_items(self):
        fake_output = io.StringIO()
        sys.stdout = fake_output

        student1 = Student(name="John Doe", id_number="1111111111")
        admin1 = Admin(name="Super Admin", id_number="1234567890")
        course1 = Course(course_code="COS101", course_name="Intro to Computer Science")

        self.display.display_items([student1, admin1, course1])
        expected_output = "Student: John Doe (1111111111)\nAdmin: Super Admin (1234567890)\nProfessor: COS101 (Intro to Computer Science)\n"

        self.assertEqual(fake_output.getvalue(), expected_output)

        sys.stdout = sys.__stdout__

    def test_display_sorted_courses(self):
        fake_output = io.StringIO()
        sys.stdout = fake_output

        course1 = Course(course_code="COS103", course_name="Data Structures and Algorithms")
        course2 = Course(course_code="COS101", course_name="Intro to Computer Science")
        course3 = Course(course_code="COS102", course_name="Programming in Python")

        self.display.display_sorted_courses([course1, course2, course3])
        expected_output = "Courses:\nCOS103: Data Structures and Algorithms\nCOS101: Intro to Computer Science\nCOS102: Programming in Python\n"

        self.assertEqual(fake_output.getvalue(), expected_output)

        sys.stdout = sys.__stdout__



if __name__ == '__main__':
    unittest.main()