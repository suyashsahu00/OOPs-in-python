# =============================================
# 🐛 DEBUG CHALLENGE 4: Polymorphism
# =============================================
# This code has 5 BUGS! Find and fix them ALL.
# Expected Output:
# Meow! 🐱
# Woof! 🐕
# Hiss! 🐍
# =============================================


class Cat:
    def speak(self):
        print("Meow! 🐱")


class Dog:
    def speak(self):
        print("Woof! 🐕")


class Snake:
    def speak(self):
        print("Hiss! 🐍")


animals = [Cat(), Dog(), Snake()]
for x in animals:
    x.speak()
