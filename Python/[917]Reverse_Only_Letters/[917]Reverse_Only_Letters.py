# Your Python code goes here.
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1 = []
        l = list(s)
        x = 0

        for i in range(len(s)):
            if s[i].isalpha():
                l1.append(s[i])
        l1.reverse()
        for i in range(len(s)):
            if l[i].isalpha():
                l[i] = l1[x]
                x = x + 1

        return "".join(l)
