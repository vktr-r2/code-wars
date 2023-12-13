"""
https://www.codewars.com/kata/587f1e1f39d444cee6000ad4

Create a Vector class with x and a y attributes that represent component magnitudes in the x and y directions.

Your vectors should handle vector additon with an .add() method that takes a second vector as an argument and returns a new vector equal to the sum of the vector you call .add() on and the vector you pass in.

For example:

>>> a = Vector(3, 4)
>>> a.x
3
>>> a.y
4
>>> b = Vector(1, 2)
>>> c = a.add(b)
>>> c.x
4
>>> c.y
6

Adding vectors when you have their components is easy: just add the two x components together and the two y components together to get the x and y components for the vector sum.

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, v2):
        sum_x = self.x + v2.x
        sum_y = self.y + v2.y

        return Vector(sum_x, sum_y)
    

# a = Vector(10, 10)
# b = Vector(10, 10)
# c = a.add(b)
# print(c.y)

        