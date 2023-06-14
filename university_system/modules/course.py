class Course:
    """
    Represents a course with a course code and course name.
    """
    def __init__(self, course_code, course_name):
        """
        Initialize a Course object with the given course code and course name.
        
        :param course_code: The course code, e.g. "CS101".
        :param course_name: The course name, e.g. "Introduction to Computer Science".
        """
        self._course_code = course_code
        self._course_name = course_name

    @property
    def course_code(self):
        """
        Return the course code.
        :return: The course code.
        """
        return self._course_code

    @course_code.setter
    def course_code(self, course_code):
        """
        Set the course code.
        :param course_code: The new course code.
        """
        self._course_code = course_code

    @property
    def course_name(self):
        """
        Return the course name.
        :return: The course name.
        """
        return self._course_name

    @course_name.setter
    def course_name(self, course_name):
        """
        Set the course name.
        :param course_name: The new course name.
        """
        self._course_name = course_name

class Enrollment:
    def __init__(self, student, course):
        """
        Initialize an Enrollment object with the given student and course.
        
        :param student: The student enrolled in the course.
        :param course: The course in which the student is enrolled.
        """
        self._student = student
        self._course = course

    @property
    def student(self):
        """
        Return the student enrolled in the course.
        :return: The student.
        """
        return self._student

    @student.setter
    def student(self, student):
        """
        Set the student enrolled in the course.
        :param student: The new student.
        """
        self._student = student

    @property
    def course(self):
        """
        Return the course in which the student is enrolled.
        :return: The course.
        """
        return self._course

    @course.setter
    def course(self, course):
        """
        Set the course in which the student is enrolled.
        :param course: The new course.
        """
        self._course = course
