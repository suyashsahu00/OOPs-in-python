# =============================================
# INTERVIEW TASK 5: Abstraction
# =============================================
# Instructions:
# 1. Import abc module (ABC and abstractmethod)
# 2. Create abstract class Notification with abstract method send(message)
# 3. Create Email class — implements send() → prints "Email sent: {message} 📧"
# 4. Create SMS class — implements send() → prints "SMS sent: {message} 📲"
# 5. Create objects and call send() on both
#
# Expected Output:
# Email sent: Welcome Suyash! 📧
# SMS sent: Your OTP is 4321 📲
# =============================================

# Write your code below 👇
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):  # abstract method — child MUST implement send()
        pass


class Email(Notification):
    def send(self, message):  # SAME name as abstract method!
        print(f"Email sent: {message} 📧")


class SMS(Notification):
    def send(self, message):  # SAME name as abstract method!
        print(f"SMS sent: {message} 📲")


e1 = Email()  # no args needed — no __init__
s1 = SMS()
e1.send("Welcome Suyash!")  # pass message when CALLING
s1.send("Your OTP is 4321")
