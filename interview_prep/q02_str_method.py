# =============================================
# Q02: Class with __str__ method
# =============================================
# Task: Create a Book class with title, author, pages
# When you print(book), it should show:
# "Harry Potter by J.K. Rowling (300 pages)"
#
# The MAGIC method __str__ controls what print() shows!

class Book:
    def __init__(self, title, author, pages):    # Q1: constructor
        self.title = title                     # Q2: store title
        self.author = author                    # Q3: store author
        self.pages = pages                     # Q4: store pages

    def __str__(self):                           # Q5: magic method for print()
        return f"{self.title} by {self.author} ({self.pages} pages)"   # Q6: return formatted string

b1 = Book("Harry Potter", "J.K. Rowling", 300)
b2 = Book("Python Crash Course", "Eric Matthes", 500)

print(b1)   # Harry Potter by J.K. Rowling (300 pages)
print(b2)   # Python Crash Course by Eric Matthes (500 pages)
