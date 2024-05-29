# Your Python code goes here.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] = nums_dict[nums[i]] + 1

        return max(nums_dict, key=nums_dict.get)
