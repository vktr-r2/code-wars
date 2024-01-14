"""
https://www.codewars.com/kata/659af96994b858db10e1675f

Given a sequence of one or more consecutive natural numbers concatenated into a string, return the smallest possible first number in the sequence. Numbers will never be truncated.

"123" -> [1, 2, 3] -> 1
"91011" -> [9, 10, 11] -> 9
"17181920" -> [17, 18, 19, 20] -> 17
"9899100" -> [98, 99, 100] -> 98
"121122123" -> [121, 122, 123] -> 121
"1235" -> [1235] -> 1235
"101" -> [101] -> 101

0 < length string < 140
0 < smallest number < 1 000 000 000

"""
import math


def find(s):

    decrement = math.floor(len(s) / 2) - 3  # < BuG TESTING.
    print(decrement)
    while decrement >= 0:
        if int(s[0:decrement]) - int(s[decrement:((decrement * 2))]) == -1:  # What if we slice from the back
            return int(s[0:decrement])
      
        decrement -= 1
        print(decrement)

    return "Logic broken"


print(find("72637236"))