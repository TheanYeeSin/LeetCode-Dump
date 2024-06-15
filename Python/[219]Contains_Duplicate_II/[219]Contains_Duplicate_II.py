# Your Python code goes here.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = {}
        for i, num in enumerate(nums):
            if num in temp and (i - temp[num]) <= k:
                return True
            else:
                temp[num] = i
        return False
