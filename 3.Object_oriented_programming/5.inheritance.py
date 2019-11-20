""" Inheritance in python enables developers to reuse code :: shorter code """


class Student:
    def __init__(self, name, campus):
        self.name = name
        self.campus = campus
        self.grades = []

    def average(self):
        """A function to calculate the average grade of a student"""
        return sum(self.grades) / (len(self.grades))


# Extend the student class to access the data in the class
class WorkingStudent(Student):
    """A class to emulate a working student"""
    def __init__(self, name, campus, salary):
        super().__init__(name, campus)
        self.salary = salary


print('')
# Create objects of the class
student_one = Student('vick', 'MIT')
student_one.grades.append(89)
student_one.grades.append(90)
student_one.grades.append(89)
student_one.grades.append(98)
student_one.grades.append(99)
print(f'Name: {student_one.name}\nCampus: {student_one.campus} \nGrades: {student_one.grades}')
print(f'{student_one.name}\'s Average grade is {student_one.average()} ')

print('')

student_two = WorkingStudent('Roseline', 'Harvard', 760000)
student_two.grades.append(89)
student_two.grades.append(99)
student_two.grades.append(87)
student_two.grades.append(96)
student_two.grades.append(100)
print(f'Name: {student_two.name}\nCampus: {student_two.campus} \nGrades: {student_two.grades}')
print(f'{student_two.name}\'s Average grade is {student_two.average()} ')
