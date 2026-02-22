class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.__marks = marks #private attribute
    def get_grade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 60:
            return "B"
        else:
            return "C"
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.get_grade()}")
        print("-"*25)

# create 2 student objects
s1 = Student("Suyash",21,85)
s2 = Student("Rahul", 20, 55)

s1.display()
s2.display()