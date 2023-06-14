import unittest
from modules.person import Person, Student, Admin


class TestPerson(unittest.TestCase):

    def test_person_name(self):
        person = Person("John Doe")
        self.assertEqual(person.name, "John Doe")
        person.name = "Jane Doe"
        self.assertEqual(person.name, "Jane Doe")

    def test_person_id_number(self):
        person = Person("John Doe", 1)
        self.assertEqual(person.id_number, 1)
        person.id_number = 2
        self.assertEqual(person.id_number, 2)

    def test_student_standing(self):
        student = Student("John Doe")
        self.assertEqual(student.standing, "freshman")
        student.standing = "sophomore"
        self.assertEqual(student.standing, "sophomore")

    def test_admin_email(self):
        admin = Admin("John Doe")
        self.assertEqual(admin.email, "fakemail.com")
        admin.email = "john.doe@example.com"
        self.assertEqual(admin.email, "john.doe@example.com")


if __name__ == '__main__':
    unittest.main()
