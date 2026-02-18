class Dog:

    def __init__(self, name, breed, owner):
        self.name = name  # Data Field
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof Whoof")


class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = (
            contact_number  # data field = phone no. parameter field = contact_number
        )


owner1 = Owner("Suyash", "India", "666-999")

# dog object and assigning it to dog variable
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(dog1.owner.name)
# dog1.bark()  # accesing method on object
# print(dog1.name)
# print(dog1.breed)
owner2 = Owner("Suyash2", "India", "666-999")

dog2 = Dog("Freya", "Greyhound", owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.name)
