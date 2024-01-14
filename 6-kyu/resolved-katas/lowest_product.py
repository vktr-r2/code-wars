"""
https://www.codewars.com/kata/554e52e7232cdd05650000a0

Create a function that returns the lowest product of 4 consecutive digits in a number given as a string.

This should only work if the number has 4 digits or more. If not, return "Number is too small".

Example
lowest_product("123456789") --> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"

"""


def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"
    
    product = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])
    i = 1
    limit = len(num)

    while i < limit - 3:
        new_product = int(num[0 + i]) * int(num[1 + i]) * int(num[2 + i]) * int(num[3 + i])

        if new_product < product:
            product = new_product

        i += 1

    return product



    


lowest_product("1234")
