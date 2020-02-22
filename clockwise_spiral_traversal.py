"""
You are given a 2D array of integers.
Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

Here is a starting point:
"""

def matrix_spiral_print(matrix, spiral=[]):
    # Iterate over last bottom row
    # Iterate over fist left colunm
    # Again

    if not matrix:
        return spiral

    i = 0

    try:
        spiral += matrix.pop(0)
        while i < len(matrix) - 1:
            spiral.append(matrix[i].pop())
            i += 1
    except IndexError:
        pass


    try:
        spiral += reversed(matrix.pop(-1))
        i = len(matrix) - 1
        while i > 0:
            spiral.append(matrix[i].pop(0))
            i -= 1
    except IndexError:
        pass
    
    return matrix_spiral_print(matrix, spiral)


grid = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

print(matrix_spiral_print(grid))
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12