# Your Python code goes here.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        highest = 0
        for num in nums:
            if num == 1:
                total += 1
            if total > highest:
                highest = total
            if num != 1:
                total = 0
        return highest
