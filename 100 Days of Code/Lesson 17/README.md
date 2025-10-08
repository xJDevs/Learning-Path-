# 🧩 What is `self` in Python (OOP)

# `self` is a reference to the current instance of the class.
# It represents the specific object that is being created or used.
# In simple terms, `self` means "this object" or "me" inside the class.

# When you define methods inside a class, `self` must always be the first parameter,
# because it allows access to the object's own attributes and methods.

# Example:
class Person:
    def __init__(self, name):
        self.name = name  # stores the name in this specific object

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Creating two different objects
p1 = Person("Johel")
p2 = Person("Randy")

# Each object has its own 'self' (own data)
p1.greet()   # Hello, my name is Johel
p2.greet()   # Hello, my name is Randy

# ✅ Key points:
# - `self` refers to the current instance (object) of the class.
# - It is passed automatically by Python (you don’t include it when calling the method).
# - It allows each object to keep and use its own data independently.
# - It’s not a reserved keyword, but it’s a strong convention to always name it `self`.