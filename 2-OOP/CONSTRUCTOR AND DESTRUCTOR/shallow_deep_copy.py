"""
🔹 Shallow Copy

Makes a new object,

But shares nested mutable objects (like lists, dicts, other class objects).

So changes in those nested objects affect the original.

🔹 Deep Copy

Makes a new object,

And also recursively copies all nested objects.

So the new object is completely independent.

Changes in the deep copy do NOT affect the original.

"""


import copy
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # marks is a list (mutable)

    def __str__(self):
        return f"Student(name={self.name}, marks={self.marks})"


# Original object
s1 = Student("Anees", [90, 85, 80])

# Shallow copy
s2 = copy.copy(s1)

# Deep copy
s3 = copy.deepcopy(s1)

print("Original:", s1)
print("Shallow:", s2)
print("Deep:", s3)

print("\n--- Modifying shallow copy's marks ---")
s2.marks[0] = 100
print("Original:", s1)
print("Shallow:", s2)
print("Deep:", s3)

print("\n--- Modifying deep copy's marks ---")
s3.marks[1] = 70
print("Original:", s1)
print("Shallow:", s2)
print("Deep:", s3)
