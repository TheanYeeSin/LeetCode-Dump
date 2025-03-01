# Your Python code goes here.
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        stack = []

        basket = ""

        for p in s:
            if p == "(":
                stack.append(p)
            else:
                stack.pop()
            basket += p
            if not stack:
                res += basket[1:-1]
                basket = ""

        return res
