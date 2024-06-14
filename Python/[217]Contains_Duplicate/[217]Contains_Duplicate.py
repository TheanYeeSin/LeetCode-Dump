# Your Python code goes here.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        temp = set()
        for num in nums:
            if num in temp:
                return True
            temp.add(num)
        return False
