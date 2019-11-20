""" @property decorator """


class Student:
    def __init__(self, name, campus):
        self.name = name
        self.campus = campus
        self.grades = []

    @property  # Use the @property decorator for functions that calculate values using properties of the object
    def average(self):
        return sum(self.grades) / (len(self.grades))


# Extend the student class to access the data in the class
class WorkingStudent(Student):
    def __init__(self, name, campus, salary):
        super().__init__(name, campus)
        self.salary = salary


student_one = Student('Victor Kamau', 'Oxford')
student_one.grades.append(89)
student_one.grades.append(90)
student_one.grades.append(89)
student_one.grades.append(98)
student_one.grades.append(99)

print(student_one.name, student_one.campus)
print(student_one.average)  # Average() can now be accessed as a normal object property
