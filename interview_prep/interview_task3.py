# =============================================
# INTERVIEW TASK 3: Inheritance
# =============================================
# Instructions:
# 1. Create a class Employee with name, salary
# 2. Add a show() method that prints name and salary
# 3. Create class Manager that INHERITS from Employee
# 4. Manager has extra attribute: department
# 5. Manager's show() should call parent's show() using super()
#    and ALSO print department
# 6. Create 1 Employee and 1 Manager, call show() on both
#
# Expected Output:
# Name: Suyash
# Salary: Rs.50000
# ---
# Name: Rahul
# Salary: Rs.80000
# Department: Engineering
# =============================================

# Write your code below 👇


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs.{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show(self):
        super().show()  # reuse parent's show!
        print(f"Department: {self.department}")


employee1 = Employee("Suyash", "50000")
manager1 = Manager("Rahul", "80000", "Engineering")
employee1.show()
manager1.show()
