# Your Python code goes here.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        reverseNum = 0
        while temp > 0:
            reverseNum = reverseNum * 10 + temp % 10
            temp = temp // 10
        return reverseNum == x
