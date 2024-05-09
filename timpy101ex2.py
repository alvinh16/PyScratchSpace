#!/usr/bin/python3

def get_largest (numbers, n) :
    numbers.sort()

    return numbers[-n:]

nums = [1, 4, 7, 9, 26, 11, 52, 37, 12, 33, 17, 19, 23]
print (nums)

largest = get_largest(nums,2)
print (nums)
