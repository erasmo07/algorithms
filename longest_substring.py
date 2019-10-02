"""
Given a string, find the length of the longest
substring without repeating characters.
"""

class Solution:
    repets = list()

    def get_substring(self, flag, letters):
        substring = list()
        while True:
            letter = letters.pop(0)
            if flag is not letter and letter not in self.repets:
                substring.append(letter)
                self.repets.append(letter)
            else:
                if flag not in self.repets:
                    substring.append(flag)
                    self.repets.append(letter)
                break
        return len(substring)

    def lengthOfLongestSubstring(self, string, longest_string=[]):
        index = 0
        lens = 0
        for letter in string:
            letters = [letter for letter in string]
            flag = letters.pop(index)
            if flag in letters:
                len_substring = self.get_substring(flag, letters)
                lens += len_substring
            index += 1
        return lens 

s = Solution()
print(s.lengthOfLongestSubstring('abrkaabcdefghijjxxx'), 10)
print(s.lengthOfLongestSubstring('abdefgabef'), 6)
print(s.lengthOfLongestSubstring('bbbb'), 1)
print(s.lengthOfLongestSubstring('geeksforgeeks'), 7)