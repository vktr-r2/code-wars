"""
https://www.codewars.com/kata/57cc847e58a06b1492000264

Given an array of numbers, return a string made up of four parts:

a four character 'word', made up of the characters derived from the first two and last two numbers in the array. order should be as read left to right (first, second, second last, last),

the same as above, post sorting the array into ascending order,

the same as above, post sorting the array into descending order,

the same as above, post converting the array into ASCII characters and sorting alphabetically.

The four parts should form a single string, each part separated by a hyphen (-).

Example format of solution: "asdf-tyui-ujng-wedg"

Examples
[111, 112, 113, 114, 115, 113, 114, 110]  -->  "oprn-nors-sron-nors"
[66, 101, 55, 111, 113]                   -->  "Beoq-7Boq-qoB7-7Boq"
[99, 98, 97, 96, 81, 82, 82]              -->  "cbRR-QRbc-cbRQ-QRbc"
"""
import functools


def sort_transform(arr):

    first_and_last_two = arr[:2] + arr[-2:]
    word = functools.reduce(lambda a, b: a + chr(b), first_and_last_two, '')

    ascending_list = sorted(arr)
    ascending_list = ascending_list[:2] + ascending_list[-2:]
    ascending_word = functools.reduce(lambda a, b: a + chr(b), ascending_list, '')

    descending_word = ascending_word[::-1]

    return f'{word}-{ascending_word}-{descending_word}-{ascending_word}'


print(sort_transform([111, 112, 113, 114, 115, 113, 114, 110]))
