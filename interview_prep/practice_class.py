# =============================================
# CODING TASK: Class & Object (Tricky!)
# =============================================
# 1. Create Student class with name, marks
# 2. is_pass() → RETURNS "Pass ✅" or "Fail ❌" (use return, not print!)
# 3. update_marks(new_marks) → updates marks, prints "Marks updated to X"
#
# ⚠️ WATCH OUT:
# - self.marks = attribute (stored)
# - new_marks = parameter (passed in) — don't write self.new_marks!
# - is_pass() uses RETURN not PRINT
#
# Expected Output:
# Suyash: Fail ❌
# Marks updated to 75
# Suyash: Pass ✅
# =============================================

# Write your code below 👇


# Test calls (write these after your class):
# s = Student("Suyash", 30)
# print(f"{s.name}: {s.is_pass()}")
# s.update_marks(75)
# print(f"{s.name}: {s.is_pass()}")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    def update_marks(self, new_marks):  # self ALWAYS first!
        self.marks = new_marks  # UPDATE the attribute!
        print(f"Marks updated to {new_marks}")


s = Student("Suyash", 30)
print(f"{s.name}: {s.is_pass()}")
s.update_marks(75)
print(f"{s.name}: {s.is_pass()}")

