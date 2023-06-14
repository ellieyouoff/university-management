import csv
from modules.person import Student, Admin
from modules.course import Course

class Loader:
    def __init__(self):
        pass

    def load_admins(self, file_path):
        """
        Loads a list of admins from a CSV file.
        :param file_path: The path to the CSV file containing the admin data.
        :return: A list of Admin objects.
        """
        admins = []

        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        admins.append(Admin(id_number=row[0], name=row[1], email=row[2]))
                    except Exception as e:
                        print(f"Error while processing row: {row}")
                        print(str(e))
        except FileNotFoundError as e:
            print("File not found:", file_path)
            raise e
        except Exception as e:
            print("Error while loading admins:", str(e))


        return admins

    def load_students(self, filename):
        """
        Loads a list of students from a CSV file.
        :param filename: The name of the CSV file containing student data.
        :return: A list of Student objects.
        """
        students = []

        try:
            with open(filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        student = Student(name=row[1], id_number=row[0], standing=row[2])
                        student.enrolled_courses = row[2:]
                        students.append(student)
                    except Exception as e:
                        print(f"Error while processing row: {row}")
                        print(str(e))
        except FileNotFoundError as e:
            print("File not found:", filename)
            raise e
        except Exception as e:
            print("Error while loading students:", str(e))

        return students

    def load_courses(self, filename):
        """
        Loads courses from a CSV file.
        :param filename: The name of the CSV file containing course data.
        :return: A list of Course objects.
        """
        courses = []

        try:
            with open(filename, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    try:
                        courses.append(Course(course_code=row[0], course_name=row[1]))
                    except Exception as e:
                        print(f"Error while processing row: {row}")
                        print(str(e))
        except FileNotFoundError as e:
            print("File not found:", filename)
            raise e
        except Exception as e:
            print("Error while loading courses:", str(e))

        return courses

    def load_students_courses(self, filename):
        """
        Loads student course data from a CSV file.
        :param filename: The name of the CSV file.
        :return: A dictionary with student ID as the key and a list of course codes as the value.
        """
        students_courses = {}

        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        student_id, course_code = row
                        if student_id not in students_courses:
                            students_courses[student_id] = []
                        students_courses[student_id].append(course_code)
                    except Exception as e:
                        print(f"Error while processing row: {row}")
                        print(str(e))
        except FileNotFoundError as e:
            print("File not found:", filename)
            raise e
        except Exception as e:
            print("Error while loading students_courses:", str(e))

        return students_courses
