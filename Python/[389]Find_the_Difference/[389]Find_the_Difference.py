# Your Python code goes here.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char not in s:
                return char
            s = s.replace(char, "", 1)
