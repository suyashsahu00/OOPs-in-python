# =============================================
# CODING TASK: Abstraction
# =============================================
# 1. Import abc module
# 2. Create abstract class Converter with abstract method convert(value)
# 3. KmToMiles: convert(km) → returns km * 0.621
# 4. CelsiusToFahrenheit: convert(c) → returns (c * 9/5) + 32
#
# ⚠️ YOUR BIGGEST MISTAKE TO AVOID:
# - Child method MUST be named convert() — NOT kmToMiles() or anything else!
# - @abstractmethod goes in PARENT only!
#
# Expected Output:
# 10 km = 6.21 miles
# 100°C = 212.0°F
# =============================================

# Write your code below 👇


# Test calls:
# k = KmToMiles()
# c = CelsiusToFahrenheit()
# print(f"10 km = {k.convert(10)} miles")
# print(f"100°C = {c.convert(100)}°F")
