# =============================================
# Q04: Inheritance — Food Ordering
# =============================================
# Task: Base class Item has name & price
# DiscountItem inherits from Item, adds discount percentage
# DiscountItem has a final_price() method

class Item:
    def __init__(self, name, price):        # Q1
        self.name = name                    # Q2
        self.price = price                    # Q3

    def show(self):
        print(f"{self.name} - Rs.{self.price}")

class DiscountItem(Item):                # Q4: inherits from?
    def __init__(self, name, price, discount):  # Q5
        super().__init__(name, price)            # Q6: call parent constructor
        self.discount = discount                    # Q7: store discount

    def final_price(self):
        cut = self.price * self.discount / 100
        return self.price - cut

d = DiscountItem("Pizza", 500, 20)
d.show()                              # Pizza - Rs.500
print(f"After 20% off: Rs.{d.final_price()}")  # After 20% off: Rs.400.0
