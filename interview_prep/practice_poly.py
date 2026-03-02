# =============================================
# CODING TASK: Polymorphism
# =============================================
# 1. Create Add, Subtract, Multiply classes
# 2. Each has calculate(a, b) that RETURNS the result
# 3. Loop and print results for 10 and 3
#
# ⚠️ WATCH OUT:
# - calculate() should RETURN, not print!
# - a, b are PARAMETERS (no self.a!)
# - Use object.method() in the loop, NOT self.method()
#
# Expected Output:
# Add: 13
# Subtract: 7
# Multiply: 30
# =============================================

# Write your code below 👇

class Add:
    def calculate(self, a, b):
        return a+b
class Subtract:
    def calculate(self, a, b):
        return a-b
class Multiply:
    def calculate(self, a, b):
        return a*b



operations = [Add(), Subtract(), Multiply()]
names = ["Add", "Subtract", "Multiply"]

for name, op in zip(names, operations):
    print(f"{name}: {op.calculate(10, 3)}")

