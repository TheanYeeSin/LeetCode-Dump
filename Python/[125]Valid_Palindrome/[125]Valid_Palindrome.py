# Your Python code goes here.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        extracted = ("".join(c for c in s if c.isalnum())).lower()
        left = 0
        right = len(extracted) - 1
        while right > left:
            if extracted[left] != extracted[right]:
                return False
            left += 1
            right -= 1
        return True
