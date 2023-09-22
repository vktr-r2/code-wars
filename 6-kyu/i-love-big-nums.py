"""

Write a function that given an array of numbers >= 0, will arrange them such that they form the biggest number.

For example:

[1, 2, 3] --> "321" (3-2-1)
[3, 30, 34, 5, 9] --> "9534330" (9-5-34-3-30)
The results will be large so make sure to return a string.

"""

"""
Python's built-in sort method prefers to use a key function to determine the sort order, 
which is a bit different from JavaScript's comparator function.

cmp_to_key: This is a utility function from the functools module. 
It converts a traditional comparator function to a key function that Python's sort can use.

SO 'str_nums.sort(key=cmp_to_key(custom_compare), reverse=True)' ENDS UP WORKING IN THESE STEPS

1. cmp_to_key(custom_compare) converts custom_compare into a key function.

2. str_nums.sort() calls this key function, behind the scenes, 
to compare each pair of elements in the array and decide their order.

3. The reverse=True parameter ensures that the largest possible concatenation comes first, 
effectively building the largest number from the elements.

"""

from functools import cmp_to_key

def custom_compare(a, b):
    ab = a + b
    ba = b + a
    return (ab > ba) - (ab < ba)

def biggest(nums):
    # If all numbers are zero, return '0'
    if all(num == 0 for num in nums):
        return '0'
    
    # Convert numbers to strings for lexicographical comparison
    str_nums = list(map(str, nums))
    
    # Custom sort the array
    str_nums.sort(key=cmp_to_key(custom_compare), reverse=True)
    
    # Concat sorted strings
    return ''.join(str_nums)