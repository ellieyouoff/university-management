import csv


class Saver:
    """
    A class responsible for saving updated data to CSV files.
    """
    def __init__(self):
        pass

    def save_students(self, file_name, students):
        """
        Save students data to a CSV file.

        :param file_name: The name of the CSV file to save data.
        :param students: A list of Student objects.
        """
        with open(file_name, "r", newline='') as csvfile:
            existing_students = set()
            reader = csv.reader(csvfile)
            for row in reader:
                existing_students.add(row[0])

        with open(file_name, "a+", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for student in students:
                if student.id_number not in existing_students:
                    csvwriter.writerow([student.id_number, student.name, student.standing])

    def save_courses(self, file_name, courses):
        """
        Save courses data to a CSV file.

        :param file_name: The name of the CSV file to save data.
        :param courses: A list of Course objects.
        """
        with open(file_name, "r", newline="") as csvfile:
            existing_courses = set()
            reader = csv.reader(csvfile)
            for row in reader:
                existing_courses.add(row[0])

        with open(file_name, "a+", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            for course in courses:
                if course.course_code not in existing_courses:
                    csvwriter.writerow([course.course_code, course.course_name])

    def save_admins(self, filename, admins):
        """
        Save admins data to a CSV file.

        :param filename: The name of the CSV file to save data.
        :param admins: A list of Admin objects.
        """
        with open(filename, "r", newline='') as file:
            existing_admins = set()
            reader = csv.reader(file)
            for row in reader:
                existing_admins.add(row[0])

        with open(filename, mode="a+", newline='') as file:
            writer = csv.writer(file)
            for admin in admins:
                if admin.id_number not in existing_admins:
                    writer.writerow([admin.id_number, admin.name, admin.email])

    def save_students_courses(self, filename, students_courses):
        """
        Save student-course enrollment data to a CSV file.

        :param filename: The name of the CSV file to save data.
        :param students_courses: A dictionary with student_id as keys and dictionaries of course_code and grade as values.
        """
        with open(filename, "r") as file:
            existing_student_course_pairs = set()
            reader = csv.reader(file)
            for row in reader:
                existing_student_course_pairs.add((row[0], row[1]))

        with open(filename, mode="a+", newline='') as file:
            writer = csv.writer(file)
            for student_id, courses in students_courses.items():
                for course_code in courses:
                    if (student_id, course_code) not in existing_student_course_pairs:
                        writer.writerow([student_id, course_code])


