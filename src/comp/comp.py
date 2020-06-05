# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        #   return f"<Human: {self.name}, {self.age}>"
        return f'{self.name}, {self.age}'


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [hum.name for hum in humans if hum.name[0] == 'D']
# for hu in humans:
#     if hu.name[0] == 'D':
#         a.append(hu)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [hum.name for hum in humans if hum.name[-1] == 'e']
# for hum in humans:
#  if hum.name[-1] == 'e':
#      b.append(hum.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
letters = ['C', 'D', 'E', 'F', 'G']
c = [hum.name for hum in humans if hum.name[0] in letters]
# for hum in humans:
#     f_letter = hum.name[0]
#     print(f_letter in letters)
#     if f_letter in letters:
#         c.append(hum.name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [hum.age + 10 for hum in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{hum.name}-{str(hum.age)}' for hum in humans]
# for hum in humans:
#     new_str = f'{hum.name}-{str(hum.age)}'
#     e.append(new_str)
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")


age = [27, 28, 29, 30, 31, 32]
f = [(hum.name, hum.age) for hum in humans if hum.age in age]

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(hum.name.upper(), hum.age + 5) for hum in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(hum.age) for hum in humans]
print(h)
