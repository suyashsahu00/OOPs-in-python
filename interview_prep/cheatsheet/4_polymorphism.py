# ================================================================
# 4️⃣ POLYMORPHISM
# ================================================================
# 📢 INTERVIEW ANSWER:
# "Polymorphism means 'many forms'. Same method name behaves differently
#  in different classes. For example, speak() works differently for
#  Cat, Dog, and Snake. This allows us to loop through different objects
#  and call the same method without knowing their exact type."


class Cat:
    def speak(self):  # 🏷️ SAME METHOD NAME in all 3 classes
        print("Meow! 🐱")


class Cow:
    def speak(self):  # Same name, DIFFERENT behavior
        print("Moo! 🐄")


class Snake:
    def speak(self):  # Same name, DIFFERENT behavior
        print("Hiss! 🐍")


# 🏷️ POLYMORPHISM IN ACTION: one loop, different behaviors
animals = [Cat(), Cow(), Snake()]
for animal in animals:
    animal.speak()  # Same method call → different output each time!
# OUTPUT: Meow! 🐱 → Moo! 🐄 → Hiss! 🐍

# ================================================================
# 📌 TERMS USED:
# Polymorphism     → "Many forms" — same method, different behavior
# Method Overriding→ Each class defines speak() its own way
# Duck Typing      → Python doesn't care about the class type,
#                     it only cares if the method exists
#                     ("If it speaks like a cat, it's a cat")
# ================================================================
