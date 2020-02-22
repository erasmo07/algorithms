"""
Given a binary tree, return all values given a certain height h.

Here's a starting point:
"""

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def getChieldRigth(root):
    rigth = None
    left = None

    if isinstance(root, list):
        return root

    if hasattr(root, 'left'):
        left = getattr(root, 'left')
    
    if hasattr(root, 'right'):
        rigth = getattr(root, 'right')
    return [left, rigth]


def valuesAtHeight(root, height):
    # Fill this in.
    if height in [0, 1]:
        return [root.value]

    levels = getChieldRigth(root)

    for _ in range(height - 2):
        levels = [getChieldRigth(level) for level in levels]
    
    values = list()
    for level in levels:
        if isinstance(level, list):
            values += [node.value for node in level if node]
        else:
            values.append(level.value)

    return values

        
    

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
assert [4, 5, 7] == valuesAtHeight(a, 3)