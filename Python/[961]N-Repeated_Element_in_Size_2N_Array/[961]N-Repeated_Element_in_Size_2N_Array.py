# Your Python code goes here.
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] in nums[i + 1 :]:
                return nums[i]
