# =============================================
# Q06: Abstraction — Payment Gateway
# =============================================
# Task: Abstract class PaymentGateway with abstract method process()
# Two child classes: Razorpay and Stripe
# Each implements process() differently

from abc import ABC, abstractmethod                    # Q1: import module & classes

class PaymentGateway(ABC):              # Q2: inherit from?
    @abstractmethod                                  # Q3: what decorator?
    def process(self, amount):
        pass

class Razorpay(PaymentGateway):                    # Q4: inherits from?
    def process(self, amount):              # Q5: implement which method?
        print(f"Razorpay: Rs.{amount} processed ✅")

class Stripe(Razorpay):                      # Q6: inherits from?
    def process(self, amount):              # Q7: implement which method?
        print(f"Stripe: ${amount} processed ✅")

# Create objects and call process()
r = Razorpay()                               # Q8: create Razorpay object
s = Stripe()                               # Q9: create Stripe object
r.process(1000)                             # Q10: call method
s.process(500)                              # Q11: call method
