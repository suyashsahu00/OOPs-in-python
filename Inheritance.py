#Inheritance = A child class acquires the properties and methods of a parent class. It promotes code reuse.
# Parents Class (Base Class)
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
#single inhereitance - student inherits form person
class Student(Person): #<- this is inheritence
    def __init__(self,fname,lname,grade):
        super().__init__(fname,lname) #call parents constructor
        self.grade = grade
    def show(self):
        print(f"{self.firstname}{self.lastname} - Grade: {self.grade}")

s = Student("Suyash","Sahu","A")
s.show()#Suyash Sahu - Grade: A
s.printname()#Suyash Sahu

#Multiple inhertence - inherits from 2 parents
class Father:
    def skill(self):
        print("Coding")
class Mother:
    def hobby(self):
        print("Painting")
class Child(Father,Mother): # <- multiple inheritance
    pass
c = Child()
c.skill() #Coding (from father)
c.hobby() #Painting (form Mother)