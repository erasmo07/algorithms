"""
Hi, here's your problem today.
This problem was recently asked by Microsoft:

You are given two linked-lists
representing two non-negative integers.

The digits are stored in reverse order
and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_values(self, l):
        value = []
        while hasattr(l, 'next'):
            value.append(str(l.val))
            l = l.next
        return value
    
    def reverse_list(self, l):
        i = 0
        while i < len(l):
            l.append(l.pop(-1))
            i += 1
        return l
        

    def addTwoNumbers(self, l1, l2, c = 0):
        values_l1 = self.reverse_list(self.get_values(l1))
        values_l2 = self.reverse_list(self.get_values(l2))

        val_l1 = int(''.join(values_l1))
        val_l2 = int(''.join(values_l2))
        val_total = str(val_l1 + val_l2)

        val_list = list(val_total)
        root = ListNode(val_list.pop())
        tmp_root = root
        while val_list:
            next_l = ListNode(val_list.pop())
            tmp_root.next = next_l
            tmp_root = tmp_root.next
        return root



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8