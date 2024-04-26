# Your Python code goes here.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        parentheses = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif char in parentheses.keys():
                if stack:
                    top_element = stack.pop()
                    if parentheses[char] != top_element:
                        return False
                else:
                    return False

        return len(stack) == 0
