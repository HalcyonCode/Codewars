""" 
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 6] --> [2, 4, 12] """

def maps(a):
    arr = []
    for i in range(0, len(a)):
        if i <= len(a)-1:
            num = a[i] * 2
            arr.append(num)
        i += 1
    return arr
