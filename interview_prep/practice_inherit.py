# =============================================
# CODING TASK: Inheritance
# =============================================
# 1. Create Shape class with color attribute
# 2. Create Circle(Shape) with radius attribute
# 3. Circle's __init__ must use super().__init__(color)
# 4. describe() prints "A {color} circle with area {area}"
#    area = 3.14 * radius * radius
#
# ⚠️ WATCH OUT:
# - Use super().__init__(color) to set parent's attribute
# - self.color comes from parent, self.radius is child's own
#
# Expected Output:
# A Red circle with area 78.5
# A Blue circle with area 28.26
# =============================================

# Write your code below 👇


# Test calls:
# c1 = Circle("Red", 5)
# c2 = Circle("Blue", 3)
# c1.describe()
# c2.describe()


class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def describe(self):  # no extra parameters!
        area = 3.14 * self.radius * self.radius  # calculate first
        print(f"A {self.color} circle with area {area}")


c1 = Circle("Red", 5)
c2 = Circle("Blue", 3)
c1.describe()
c2.describe()
