# Your Python code goes here.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = []
        for i in range(0, len(nums)):
            if nums[i] not in array:
                array.append(nums[i])
            else:
                array.pop(array.index(nums[i]))
        return array[0]
