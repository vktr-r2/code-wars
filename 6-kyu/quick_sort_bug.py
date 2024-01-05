"""
https://www.codewars.com/kata/56bdaa2cbe8f29257c000085

There is an implementation of quicksort algorithm. Your task is to fix it.
All inputs are correct.

See also: https://en.wikipedia.org/wiki/Quicksort
"""


def quicksort(arr):
    if len(arr) < 1: return arr
    p = arr[0]
    return quicksort(map(lambda x: x < p, arr[::-1])) + quicksort(map(lambda x: x > p, arr[2:]))

# TypeError: object of type 'map' has no len()
