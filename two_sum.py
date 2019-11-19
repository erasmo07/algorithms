"""
You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list
that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5, 
return true since 4 + 1 = 5.
"""

def two_sum(list_, k):
    index = list_.pop(0)
    search = False
    for item in list_:
        if index + item == k:
            search = True
            break
    else:
        two_sum(list_, k)
    return search


assert(two_sum([4,7,1,-3,2], 5))