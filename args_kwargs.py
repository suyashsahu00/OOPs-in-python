# *args → accepts any number of POSITIONAL arguments (stored as tuple)
from os import name
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Suyash", "Hero", "SuyashH")  #  The youngest child is SuyashH

# **kwargs -> accepts any number of keyword argumentts (stored in dict)
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Both together!
def combined(*args, **kwargs):
    print("Args:",args)
    print("kwargs:",kwargs)
combined(1,2,3, name="Suyash",age= 21)
# Args: (1,2,3)
# Kwargs: {'name': 'suyash','age':21}