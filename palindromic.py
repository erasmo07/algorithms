"""
A palindrome is a sequence of characters that reads 
the same backwards and forwards.

Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""

class Solution: 
    def longestPalindrome(self, string):
        substring = list()
        letters = [letter for letter in string]
        while letters:
            flag = letters.pop(0)
            if flag in letters:
                substring.append(flag)
                for letter in letters:
                    if letter is flag:
                        substring.append(letter)
                        break
                    else:
                        substring.append(letter)
                break
        return "".join(substring)


      # Fill this in.
        
# Test program
print(Solution().longestPalindrome("tracecars"), 'racecar')
print(Solution().longestPalindrome("banana"), 'anana')
print(Solution().longestPalindrome("million"), 'illi')