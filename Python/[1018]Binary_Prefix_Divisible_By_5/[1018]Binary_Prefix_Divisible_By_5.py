# Your Python code goes here.
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        num = 0

        for n in nums:
            num = (num * 2 + n) % 5
            res.append(num == 0)

        return res
