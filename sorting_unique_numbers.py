"""
Given a list of numbers with only 3 unique 
numbers (1, 2, 3), sort the list in O(n) time.

Example:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
"""

def sortNums(nums, sort_numbers=list(), unique_numbers=[1,2,3]):
    index = 0
    unique_number = unique_numbers.pop(0)
    while index is not len(nums):
        if nums[index] == unique_number:
            sort_numbers.append(nums.pop(index))
        else:
            index += 1
    
    if unique_numbers:
        sortNums(
            nums=nums,
            sort_numbers=sort_numbers,
            unique_numbers=unique_numbers)
    return sort_numbers


assert(sortNums([3, 3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3, 3])