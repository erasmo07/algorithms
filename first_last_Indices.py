"""
Hi, here's your problem today.
This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements,
find the indices of the first and last occurrences of a target
element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
"""

class Solution: 
    def getRange(self, arr, target):
        # Fill this in.
        indexs = list()
        for index, element in enumerate(arr):
            if element != target:
                continue
            
            if len(indexs) > 1:
                indexs.pop()
            
            indexs.append(index)
        else:
            if len(indexs) is 0:
                indexs = [-1, -1]
        return indexs
  
# Test program 
solution = Solution()
assert(solution.getRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2) == [1, 4])
assert(solution.getRange([1,3,3,5,7,8,9,9,9,15], 9) == [6, 8])
assert(solution.getRange([100, 150, 150, 153], 150) == [1, 2])
assert(solution.getRange([1,2,3,4,5,6,10], 9) == [-1, -1])
print('Works')
