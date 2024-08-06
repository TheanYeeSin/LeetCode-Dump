# Your Python code goes here.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums.sort()
        while nums != []:
            num1 = nums.pop()
            num2 = nums.pop()
            total += num2
        return total
