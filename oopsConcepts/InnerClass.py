class Employee:
    def __init__(self, sid, ename, brand):
        self.sid = sid
        self.ename = ename
        self.laptop = self.Laptop(brand)        # calling inner class inside outer class and passing value to it

    def show(self):
        print(self.sid, self.ename)
        self.laptop.show()

    class Laptop:
        def __init__(self, brand):
            self.brand = brand

        def show(self):
            print('Inner class var: ', self.brand)


emp1 = Employee(101, 'Arpita', 'Macbook')       # implicitly calling inner class
emp2 = Employee(102, 'Saikat', 'Dell')
emp1.show()
emp2.show()

laptopOutside = Employee.Laptop('Acer')         # explicitly calling inner class
laptopOutside.show()
