"""
You are given a 2D array of characters, and a target string.
Return whether or not the word target word exists in the matrix.
Unlike a standard word search, the word must be either going 
left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM,
you should return true, as it can be found 
going up-to-down in the first column.

Here's the function signature:
"""

def word_search(matrix, word):
    # Itereate to matrix
    # Create three variables position, right_word, bottom_word
    # Assign variables to correct position
    # Evaluate if right_word is the next word
        # iterate to right words
    # Evaluate if bottom_word is the next word
        # Iterate to bottom words
    # Move position and repet all
    find = False
    position = 0
    next_vertical = 0
    right_word = None
    bottom_word = None
    index_vertical, index_horizontal = (1, 1)
    while next_vertical < len(matrix):
        is_not_next_vertical = word[position] != matrix[position][next_vertical]
        is_not_next_horizontal = word[position] != matrix[next_vertical][position]
        if is_not_next_vertical and is_not_next_horizontal:
            next_vertical += 1
            continue

        right_word = matrix[position][index_horizontal]
        if word[index_horizontal] == right_word:
            while index_horizontal < len(matrix) - 1:
                index_horizontal += 1
                if word[index_horizontal] != matrix[position][index_horizontal]:
                    break
                continue
            if index_horizontal == len(matrix) - 1:
                find = True
        
        if find:
            break

        bottom_word = matrix[index_vertical][position]
        if word[index_vertical] == bottom_word:
            while index_vertical < len(matrix) - 1:
                index_vertical += 1
                if word[index_horizontal] != matrix[index_horizontal][position]:
                    break
                continue
            if index_vertical == len(matrix) - 1:
                find = True
        
        if find:
            break

        position += 1
        next_vertical = 0
    return find



matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
print(word_search(matrix, 'FACI'))
print(word_search(matrix, 'MASS'))
print(word_search(matrix, 'MASA'))
