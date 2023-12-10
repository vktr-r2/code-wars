# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
"""

def remove_char(s):
    char_list = list(s)                     ## Split string into list
    char_list.pop(0)                        ## Remove first item in list
    char_list.pop(-1)                       ## Remove last item in list
    new_string = "".join(char_list)         ## Join list back into string
    return new_string