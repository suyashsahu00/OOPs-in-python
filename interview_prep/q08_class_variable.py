# =============================================
# Q08: Class Variable vs Instance Variable
# =============================================
# Task: Create a Student class where:
# - total_students is a CLASS variable (shared by ALL objects)
# - name and marks are INSTANCE variables (unique to each object)
# - Every time a new Student is created, total_students increases by 1


class Student:
    total_students = 0  # Q1: class variable (no self!)

    def __init__(self, name, marks):  # Q2: constructor
        self.name = name  # Q3: instance variable
        self.marks = marks  # Q4: instance variable
        Student.total_students += 1  # Q5: increase class variable (ClassName.variable)

    def show(self):
        print(f"{self.name} scored {self.marks}")


s1 = Student("Suyash", 85)
s2 = Student("Rahul", 92)
s3 = Student("Priya", 78)

s1.show()
s2.show()
s3.show()
print(f"Total students: {Student.total_students}")  # Q6: ClassName.class_variable
# Expected:
# Suyash scored 85
# Rahul scored 92
# Priya scored 78
# Total students: 3
