"""
Given a string, find the length of the longest
substring without repeating characters.
"""

class Solution:

    def get_substring(self, flag, letters):
        substring = list()
        repets = list()
        index = 1
        while index < len(letters):
            letter = letters[index]
            if flag is not letter:
                if letter not in repets:
                    substring.append(letter)
                    repets.append(letter)
            else:
                substring.append(flag)
                break
            index += 1
        return len(substring)

    def lengthOfLongestSubstring(self, string):
        index = 0
        len_substring = 0
        while index < len(string):
            flag = string[index]
            if flag in string[index+1:]:
                substring = self.get_substring(flag, string[index:])
                if substring > len_substring:
                    len_substring = substring 
            index += 1
        return len_substring

s = Solution()
print(s.lengthOfLongestSubstring('abrkaabcdefghijjxxx'), 10)
print(s.lengthOfLongestSubstring('abdefgabef'), 6)
print(s.lengthOfLongestSubstring('bbbb'), 1)
print(s.lengthOfLongestSubstring('geeksforgeeks'), 7)
