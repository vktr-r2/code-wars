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


def find(s):
    # Length of the string
    length = len(s)

    for i in range(1, length // 2 + 1):
        # Starting number
        start_num = int(s[:i])
        num = start_num

        # Generate consecutive number string
        generated = ''
        while len(generated) < length:
            generated += str(num)
            num += 1

        # Check if the generated string matches the input string
        if generated == s:
            return start_num

    # If no consecutive sequence found, return the entire string as a number
    return int(s)