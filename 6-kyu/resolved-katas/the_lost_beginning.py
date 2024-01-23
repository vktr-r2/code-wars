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

# DOUBLE LOOP (ITERATE FROM FRONT)


def find(s):
    # Length of the string
    length = len(s)

    # Setup range of numbers from 1 to the floor of length / 2 , add 1
    for i in range(1, length // 2 + 1):
        # Starting number takes characters at index 0 to 1
        start_num = int(s[:i])
        # Number = start_num
        num = start_num

        # Define a test string variable
        generated = ''
        # While the length of my generated test string is less than the length of 's' argument string
        while len(generated) < length:
            # Over and over add num + 1 to the string
            generated += str(num)
            num += 1

        # Check if the test string matches 's' argument string
        if generated == s:
            # if true, return the original starting number
            return start_num

    # If no consecutive sequence found, return the entire string as a single number
    return int(s)