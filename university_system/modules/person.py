class Person:
    """
    A generic Person class, used as a base class for Student, and Admin.
    """
    _instances = []

    def __init__(self, name, id_number=None):
        """
        Initialize a new Person instance with a given name
        and an optional unique ID number.

        :param name: The name of the person.
        :param id_number: (Optional) A unique ID number for the person.
            If not provided, a unique ID will be generated.
        """
        self._name = name
        self._id_number = id_number
        Person._instances.append(self)

    @property
    def name(self):
        """
        Get the name of the person.

        :return: The name of the person.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the name of the person.

        :param value: The new name for the person.
        """
        self._name = value

    @property
    def id_number(self):
        """
        Get the ID number of the person.

        :return: The ID number of the person.
        """
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        """
        Set the ID number of the person.

        :param value: The new ID number for the person.
        """
        self._id_number = value


class Student(Person):
    """
    A Student class, derived from Person, representing a student in
    the University Management System.
    """

    def __init__(self, name, id_number=None, standing='freshman'):
        """
        Initialize a new Student instance with a given name,
        an optional unique ID number, and an optional class standing.

        :param name: The name of the student.
        :param id_number: (Optional) A unique ID number for the student.
            If not provided, a unique ID will be generated.
        :param standing: (Optional) The student's class standing.
            If not provided, the default value is 'freshman'.
        """
        super().__init__(name, id_number)
        self._standing = standing

    @property
    def standing(self):
        """
        Get the class standing of the student.

        :return: The class standing of the student.
        """
        return self._standing

    @standing.setter
    def standing(self, value):
        """
        Set the class standing of the student.

        :param value: The new class standing for the student.
        """
        self._standing = value


class Admin(Person):
    """
    An Admin class, derived from Person, representing an administrator
    in the University Management System.
    """

    def __init__(self, name, id_number=None, email="fakemail.com"):
        """
        Initialize a new Admin instance with a given name,
        an optional unique ID number, and an optional email address.

        :param name: The name of the admin.
        :param id_number: (Optional) A unique ID number for the admin.
            If not provided, a unique ID will be generated.
        :param email: (Optional) The email address of the admin.
            If not provided, the default value is 'fakemail.com'.
        """
        super().__init__(name, id_number)
        self._email = email

    @property
    def email(self):
        """
        Get the email address of the admin.

        :return: The email address of the admin.
        """
        return self._email
    
    @email.setter
    def email(self, value):
        """
        Set the email address of the admin.

        :param value: The new email address for the admin.
        """
        self._email = value

