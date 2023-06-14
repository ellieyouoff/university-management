import unittest
from modules.course import Course, Enrollment
from modules.person import Student


class TestCourse(unittest.TestCase):

    def test_course_code(self):
        course = Course("CS101", "Introduction to Computer Science")
        self.assertEqual(course.course_code, "CS101")
        course.course_code = "CS102"
        self.assertEqual(course.course_code, "CS102")

    def test_course_name(self):
        course = Course("CS101", "Introduction to Computer Science")
        self.assertEqual(course.course_name, "Introduction to Computer Science")
        course.course_name = "Data Structures"
        self.assertEqual(course.course_name, "Data Structures")

    def test_enrollment_student(self):
        student = Student("John Doe")
        course = Course("CS101", "Introduction to Computer Science")
        enrollment = Enrollment(student, course)
        self.assertEqual(enrollment.student, student)
        new_student = Student("Jane Doe")
        enrollment.student = new_student
        self.assertEqual(enrollment.student, new_student)

    def test_enrollment_course(self):
        student = Student("John Doe")
        course = Course("CS101", "Introduction to Computer Science")
        enrollment = Enrollment(student, course)

        self.assertEqual(enrollment.course, course)
        new_course = Course("CS102", "Data Structures")
        enrollment.course = new_course
        self.assertEqual(enrollment.course, new_course)


if __name__ == '__main__':
    unittest.main()

