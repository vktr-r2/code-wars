"""

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

"""
# MY SOLUTION
def find_it(seq):
    
    # Define dictionary to count number of occurances
    counter = {}
    

    """'counter.get(ele, 0)' : This method returns the value for the given key 
    ele if it exists in the dictionary. If the key does not exist, 
    it returns the default value 0.

    '+ 1' : This part increments the count by 1. So, if ele already exists in the dictionary, its count will be incremented. 
    If it does not exist, the get() method returns 0, and then 0 + 1 will be 1.

    'counter[ele] =' : Finally, the updated count is stored back in the dictionary 
    at the key ele."""

    for ele in seq:
        counter[ele] = counter.get(ele, 0) + 1

    # Check if value is odd, if so return key
    for key in counter:
        if counter[key] % 2 != 0:
            return key