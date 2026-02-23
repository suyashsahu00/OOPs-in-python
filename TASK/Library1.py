from random import random
import random

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]

print(random.choice(fruits))

random.shuffle(fruits)
print(fruits)
