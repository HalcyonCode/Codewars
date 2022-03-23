""" You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0. """

def pos_sum(arr):
    pSum = 0
    for i in range(0, len(arr)):
        if i <= len(arr)-1 and arr[i] > 0:
            pSum += arr[i]     
        i += 1       
    return pSum