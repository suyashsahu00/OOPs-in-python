class Dog:

    def __init__(self, name, breed):
        self.name = name  # Data Field
        self.breed = breed

    def bark(self):
        print("Whoof Whoof")


# dog object and assigning it to dog variable
dog1 = Dog("Brue", "Scottish Terrier")
dog1.bark()  # accesing method on object
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Freya", "Greyhound")
dog2.bark()
print(dog2.name)
print(dog2.breed)