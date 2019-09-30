"""
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807

Here is the function signature as a starting point (in Python):
"""


def get_val_list_node(list_node, vals=[]):
    vals.append(list_node.val)
    if list_node.next:
        get_val_list_node(list_node.next, vals)
    return vals


def linked_list_node(list_values, principal_node):
    list_node = ListNode(list_values.pop())
    principal_node.next = list_node
    if len(list_values) is not 0:
        linked_list_node(list_values, list_node)


def list_to_int(vals, result=""):
    for val in vals:
        result += str(val)
    return int(result)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        val_l1 = get_val_list_node(l1, vals=[])
        val_l1.reverse()

        val_l2 = get_val_list_node(l2, vals=[])
        val_l2.reverse()

        integer1 = list_to_int(val_l1)
        integer2 = list_to_int(val_l2)

        result = integer1 + integer2
        principal_node = ListNode(result)

        result_string = str(result)
        result_list = [int(s) for s in result_string]
        linked_list_node(result_list, principal_node)
        return principal_node


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
