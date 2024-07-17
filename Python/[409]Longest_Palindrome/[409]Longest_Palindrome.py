# Your Python code goes here.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        chars = []
        for c in s:
            if c in chars:
                index = chars.index(c)
                chars.pop(index)
                total += 2
            else:
                chars.append(c)
        if chars:
            total += 1
        return total
