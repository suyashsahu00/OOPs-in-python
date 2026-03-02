# =============================================
# CODING TASK: Encapsulation (Tricky!)
# =============================================
# 1. Create Password class with PRIVATE __password
# 2. verify(attempt) → returns True if matches, False if not
# 3. change_password(old, new) → changes ONLY if old matches current
#
# ⚠️ WATCH OUT:
# - old, new, attempt = PARAMETERS (no self.!)
# - self.__password = ATTRIBUTE (stored)
#
# Expected Output:
# True
# False
# Password changed! ✅
# Wrong old password! ❌
# True
# =============================================

# Write your code below 👇


# Test calls:
# p = Password("python123")
# print(p.verify("python123"))         # True
# print(p.verify("wrong"))             # False
# p.change_password("python123", "newpass456")    # Password changed! ✅
# p.change_password("python123", "hack")          # Wrong old password! ❌
# print(p.verify("newpass456"))         # True

class Password:
    def __init__(self, password):
        self.__password =password 
    def verify(self, attempt):
        if attempt ==self.__password:
            return True
        else:
            return False
    def change_password(self, old, new):
        if self.verify(old):
            self.__password = new
            print("Password Changed!")
        else:
            print("Wrong old passsword!")

p = Password("python123")
print(p.verify("python123"))
#True
print(p.verify("wrong"))
p.change_password("python123","newpass456")
p.change_password("python123", "hack")
print(p.verify("newpass456"))