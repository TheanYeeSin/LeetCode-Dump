# Your Python code goes here.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(0, len(digits)):
            num = num * 10 + digits[i]
        num = num + 1
        return [int(x) for x in str(num)]
