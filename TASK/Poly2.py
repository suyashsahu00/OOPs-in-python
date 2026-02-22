class Cat:
    def speak(self):  # self is always required!
        print("Meow! 🐱")


class Cow:
    def speak(self):  # self is always required!
        print("Moooo! 🐄")


class Snake:
    def speak(self):  # self is always required!
        print("Hisssss! 🐍")


animals = [Cat(), Cow(), Snake()]  # renamed list to 'animals' to avoid confusion
for animal in animals:
    animal.speak()  # object.method() ← correct!
