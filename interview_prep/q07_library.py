# =============================================
# Q07: Mini Library System
# =============================================
# Task: Create a Book class with:
# - Private attribute __is_available (default True)
# - Method borrow() → if available, mark as borrowed. If not, say "Already borrowed!"
# - Method return_book() → mark as available again
# - __str__ shows: "Python 101 by Suyash [Available]" or "[Borrowed]"


class Book:
    def __init__(self, title, author):  # Q1
        self.title = title  # Q2
        self.author = author  # Q3
        self.__is_available = True  # Q4: private! default True

    def borrow(self):
        if self.__is_available:  # Q5: check private attribute
            self.__is_available = False  # Q6: set to False (borrowed!)
            print(f"'{self.title}' borrowed ✅")
        else:  # Q7: keyword
            print(f"'{self.title}' already borrowed! ❌")

    def return_book(self):
        self.__is_available = True  # Q8: set back to True
        print(f"'{self.title}' returned ✅")

    def __str__(self):  # Q9: magic method — needs __!
        status = "Available" if self.__is_available else "Borrowed"  # Q10
        return f"{self.title} by {self.author} [{status}]"


b = Book("Python 101", "Suyash")
print(b)  # Python 101 by Suyash [Available]
b.borrow()  # 'Python 101' borrowed ✅
print(b)  # Python 101 by Suyash [Borrowed]
b.borrow()  # 'Python 101' already borrowed! ❌
b.return_book()  # 'Python 101' returned ✅
print(b)  # Python 101 by Suyash [Available]
