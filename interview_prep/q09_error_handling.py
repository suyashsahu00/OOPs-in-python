# =============================================
# Q09: Error Handling — Safe Calculator
# =============================================
# Task: Create a Calculator class that handles errors
# - divide() should handle division by zero
# - No crashes allowed!


class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        try:  # Q1: keyword to TRY risky code
            result = a / b
            print(f"{a} / {b} = {result}")
        except ZeroDivisionError:  # Q2: keyword to CATCH the error
            print("Cannot divide by zero! ❌")
        except Exception as e:  # Q3-Q4: catch ALL other errors
            print(f"Error: {e}")


calc = Calculator()  # Q5: create object
print(calc.add(10, 5))  # Q6: call add method → 15
calc.divide(10, 2)  # Q7: call divide → 10 / 2 = 5.0
calc.divide(10, 0)  # Q8: call divide → Cannot divide by zero! ❌
