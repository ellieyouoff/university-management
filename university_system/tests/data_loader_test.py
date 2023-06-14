import unittest

from modules.data_loader import Loader
from modules.person import Student, Admin
from modules.course import Course

class TestLoader(unittest.TestCase):

    def setUp(self):
        self.loader = Loader()

    def test_load_admins(self):
        admins = self.loader.load_admins('admins.csv')
        self.assertIsInstance(admins, list)
        self.assertIsInstance(admins[0], Admin)

        # Test exception handling for file not found
        with self.assertRaises(FileNotFoundError):
            self.loader.load_admins('nonexistent_file.csv')

    def test_load_students(self):
        students = self.loader.load_students('students.csv')
        self.assertIsInstance(students, list)
        self.assertIsInstance(students[0], Student)

        # Test exception handling for file not found
        with self.assertRaises(FileNotFoundError):
            self.loader.load_students('nonexistent_file.csv')

    def test_load_courses(self):
        courses = self.loader.load_courses('courses.csv')
        self.assertIsInstance(courses, list)
        self.assertIsInstance(courses[0], Course)

        # Test exception handling for file not found
        with self.assertRaises(FileNotFoundError):
            self.loader.load_courses('nonexistent_file.csv')


    def test_load_students_courses(self):
        students_courses = self.loader.load_students_courses('students_courses.csv')
        self.assertIsInstance(students_courses, dict)

        # Test exception handling for file not found
        with self.assertRaises(FileNotFoundError):
            self.loader.load_students_courses('nonexistent_file.csv')

if __name__ == '__main__':
    unittest.main()
