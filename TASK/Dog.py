class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says: Woof!")
        print(f"Breed :{self.breed} ")
        

d1 = Dog("Buddy","Labrador")
d1.bark()