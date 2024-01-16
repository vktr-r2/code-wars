"""
DESCRIPTION:
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

# First attempt not working when multiple uppercase characters exist in string
# def solution(s):

#     for index, char in enumerate(s):
#         print(index)
#         if char.isupper():
#             s = s[:index] + " " + s[index:]

#     return s

# Second attempt not working when multiple uppercase characters exist in string


def solution(s):

    uppercase_indicies = []
    tally = 0

    for index, char in enumerate(s):
        if char.isupper():
            uppercase_indicies.append(index)

    for index in uppercase_indicies:
        s = s[:index + tally] + " " + s[index + tally:]
        tally += 1

    return s


print(solution("camelCasingTestString"))
