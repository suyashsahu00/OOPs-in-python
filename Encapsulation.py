#Encapusaltion is hiding internal details and exposing only what's is necessary
class BankAccount:
    def __init__(self):
        self.name = "Suaysh" #Public -> accesible to all
        self._balance = 1000 #protected -> convention, use with care
        self.__pin = 1234 # private ->  hidden

    #Getter method - controlled access
    def get_pin(self):
        return "access denied"

    #Setter method - controlled modification
    def set_pin(self, old_pin,new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("Pin updated")
        else:
            print("Wrong pin")
acc = BankAccount()
print(acc.name)
print(acc._balance)
#print(acc.__pin) #Attributeerror
acc.set_pin(1234,5678)