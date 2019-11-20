"""
 Object oriented programing allow programs to imitate the objects in the real world
"""

"""
Create a student dict with name and grades and write a function to calculate the average grade of the student
"""


def main():
    student = {
        'name': 'vick Kamau',
        'grades': [90, 100, 98, 97, 96]
    }

    def calculate_average(grades):
        average = grades / len(student['grades'])
        return average

    total = sum(student['grades'])
    print(calculate_average(total))

    """
    Instead of using a dictionary, now use a class to represent the student.
    --> Dictionaries cannot contain that act on their data but classes can
    --> Multiple independent objects can be created from one class
    --> A class is a blueprint for creating objects
    --> An object is a class variable or an instance of the class
    """

    class Student:
        """ a class to represent a student..it models a students with a name and grades"""

        def __init__(self, names, grades):  # The __init__() function is a constructor for the class student
            self.name = names
            self.grade = grades

        def calculate_average(self):
            """A function to calculate the average of a students grades"""
            average = sum(self.grade) / len(self.grade)
            return average

    # Objects of the student class
    student_one = Student('Victor Kamau', [90, 96, 98, 97, 100])
    student_two = Student('Lucy Njeri', [89, 98, 78, 89, 96])

    # Accessing the fields in the objects
    print('')

    print(student_one.name)
    print(student_one.grade)
    print(f'{student_one.name}\'s average grade is {student_one.calculate_average()}')

    print('')

    print(student_two.name)
    print(student_two.grade)
    print(f'{student_two.name}\'s average grade is {student_two.calculate_average()}')


if __name__ == '__main__':
    main()
