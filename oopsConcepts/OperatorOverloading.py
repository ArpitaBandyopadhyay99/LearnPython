class Student:
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name

    def __add__(self, other):
        obj1 = self.marks + other.marks
        return obj1

    def __str__(self):
        return "{} {}".format(self.marks, self.name)


stud1 = Student(90, "AB")
stud2 = Student(100, "XY")

print(stud1)
print(stud2)

stud3 = stud1 + stud2
print(stud3)
