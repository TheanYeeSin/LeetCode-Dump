class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_indices:
                return [nums_indices[complement], i]
            nums_indices[num] = i
        return None
