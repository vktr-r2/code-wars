"""
https://www.codewars.com/kata/57f7e7617a28db2a2200021a

Task:
Given a list of integers l, return the list with each value multiplied by integer n.

Restrictions:

    The code must not:

    contain *.
    use eval() or exec()
    contain for
    modify l

Happy coding :)
"""

# DOES NOT WORK
def multiply(n, l):
    return list(map(lambda x: sum([x] * n), l))