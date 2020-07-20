class Student:
    school = "Kendriya Vidyalaya"

    def __init__(self, math, science, english):
        self.mathMark = math
        self.scienceMark = science
        self.englishMark = english

    def total_marks(self):
        print(self.mathMark + self. scienceMark + self.englishMark)

    @classmethod
    def fetch_school_name(cls):
        print("Class method, school name: ", cls.school)

    @staticmethod
    def display_blah():
        print("Blah blah blah...")


# create object outside of class student
std1 = Student(90, 90, 90)
std2 = Student(40, 40, 40)

std1.total_marks()              # instance method
std2.total_marks()              # instance method

Student.fetch_school_name()     # class method

Student.display_blah()          # static method - does not depends on class/instance variable

Student.total_marks(std2)       # bad signature to call instance method
