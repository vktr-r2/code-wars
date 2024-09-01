"""

Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""


"""
MY ORIGINAL SOLUTION

# Import regular expression module
import re


def XO(s):
    
    # Searches for all occurrences of "x" in the string s, case-insensitively. 
    x = re.findall(r'x', s, re.IGNORECASE)
    o = re.findall(r'o', s, re.IGNORECASE)

    # Compares the lengths of the lists x and o to see if they're equal,
    return len(x) == len(o)
"""

# BETTER SOLUTION
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')