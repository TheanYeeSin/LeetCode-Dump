# Your Python code goes here.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        a = 0
        for i in range(0, len(s)):
            if s[len(s) - 1 - i] != " ":
                a += 1
            else:
                break

        return a
