"""
https://www.codewars.com/kata/56bdaa2cbe8f29257c000085

There is an implementation of quicksort algorithm. Your task is to fix it.
All inputs are correct.

See also: https://en.wikipedia.org/wiki/Quicksort
"""


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p = arr[0]
        # filter elements less than or equal to first element into "less" list
        less = filter(lambda x: x <= p, arr[1:])

        # filter elements greater than first element into "greater" list
        greater = filter(lambda x: x > p, arr[1:])

        # return a combined list of "less" + original first element + "greater"
        # call recursively until length of less or greater lists is 1 or less
        return quicksort(list(less)) + [p] + quicksort(list(greater))


