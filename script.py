class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")


person1 = Person("Suyash",30)
person1.greet()

person2 = Person("Suyash2",30)
person2.greet()