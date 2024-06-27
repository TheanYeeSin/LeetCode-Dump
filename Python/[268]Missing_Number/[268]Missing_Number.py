# Your Python code goes here.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sum_original = N * (N + 1) / 2
        sum_given = sum(nums)
        return int(sum_original - sum_given)
