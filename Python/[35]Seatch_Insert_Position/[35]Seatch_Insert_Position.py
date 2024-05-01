# Your Python code goes here.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # O(logN) approach
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

        # O(n) approach
        # k = 0
        # for i in range(0, len(nums)):
        #     if target > nums[i]:
        #         k += 1
        #     else:
        #         continue
        # return k
