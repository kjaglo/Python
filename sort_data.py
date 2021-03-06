fruit = ["orange", "banana", "strawberry", "apple", "cherry"]

print(fruit)

fruit.sort()  # ascending order
print(fruit)  # ['apple', 'banana', 'cherry', 'orange', 'strawberry']

fruit.sort(reverse=True)  # descending order
print(fruit)  # ['strawberry', 'orange', 'cherry', 'banana', 'apple']

fruit_tuple = ("orange", "banana", "strawberry", "apple", "cherry")
# tuble has no attribute 'sort'
# tuples are immutable objects (they cannot be changed)
help(list.sort)
# sort(self, /, *, key=None, reverse=False)
# Stable sort *IN PLACE*.

# in place - does not create a second data structure
# sort changes the list itself

# ("name", radius, density, distance from Sun),

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.0),
    ("Mars", 3396, 3.93, 1.53),
    ("Jupiter", 71492, 1.33, 5.21),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.07),
]

radius = lambda planet: planet[1]
planets.sort(key=radius, reverse=True)
print(planets)

dens = lambda planet: planet[2]
planets.sort(key=dens, reverse=True)
print(planets)

help(sorted)

# sorted(iterable, /, *, key = None, reverse = False)
# Return a new list containing all items from the iterable in ascending order.
#
# A custom key function can be supplied to customize the
# sort order, and the reverse flag can be set to request
# the  result in descending order.

planets_sorted = sorted(planets)
print(planets)
print(planets_sorted)

tuple_int = (1, 9, 2, 3, 4, 7, 6, 5, 8)
tuple_int_sorted = sorted(tuple_int)
print(tuple_int_sorted)  # sorted list: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sorted("Python is cool"))
# [' ', ' ', 'P', 'c', 'h', 'i', 'l', 'n', 'o', 'o', 'o', 's', 't', 'y']
