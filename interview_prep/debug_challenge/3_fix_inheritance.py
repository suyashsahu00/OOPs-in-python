# =============================================
# 🐛 DEBUG CHALLENGE 3: Inheritance
# =============================================
# This code has 5 BUGS! Find and fix them ALL.
# Expected Output:
# Name: Suyash
# Salary: Rs.50000
# Name: Rahul
# Salary: Rs.80000
# Department: Engineering
# =============================================


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs.{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)
        self.department = department

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs.{self.salary}")
        print(f"Department: {self.department}")


e = Employee("Suyash", 50000)
m = Manager("Rahul", 80000, "Engineering")
e.show()
m.show
