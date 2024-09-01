"""

DESCRIPTION:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

def solution(string):

    result = []                             # Introduce result list to be returned
    
    while string:                           # Loop runs while string is still truthy.  Empty string "" would evaluate to falsy
        if len(string[:2]) < 2:             # If slicing the strings first two characters returns one character
            string += "_"                       # Concatenate "_"
        result.append(string[:2])           # Append the first two characters to results list
        string = string[2:]                 # Remove first two characters by assigning string back to itself 

    return result                           # Return result
    
print(solution("Hello, world!"))
    
