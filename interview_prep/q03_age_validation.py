# =============================================
# Q03: Encapsulation — Age Validation
# =============================================
# Task: Create a Person class where age is PRIVATE
# Add a set_age() method that VALIDATES before setting
# - If age < 0 or age > 150 → print "Invalid age!"
# - Otherwise → set the age and print "Age set to X"


class Person:
    def __init__(self, name):  # Q1: constructor
        self.name = name  # Q2: store name
        self.__age = 0  # Q3: make age PRIVATE (what prefix?)

    def set_age(self, age):  # Q4: what parameter?
        if age < 0 or age > 150:  # Q5: check the parameter
            print("Invalid age! ❌")
        else:  # Q6: what keyword?
            self.__age = age  # Q7: age is the PARAMETER, self.__age is the ATTRIBUTE
            print(f"Age set to {self.__age} ✅")

    def get_age(self):  # Q8: what parameter?
        return self.__age  # Q9: return private age


p = Person("Suyash")
p.set_age(21)  # Age set to 21 ✅
p.set_age(-5)  # Invalid age! ❌
p.set_age(200)  # Invalid age! ❌
print(p.get_age())  # 21
