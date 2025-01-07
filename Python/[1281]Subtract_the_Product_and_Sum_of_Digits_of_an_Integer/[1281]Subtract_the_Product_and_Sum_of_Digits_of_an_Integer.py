# Your Python code goes here.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = str(n)

        prod = 1
        sum = 0

        for num in x:
            prod *= int(num)
            sum += int(num)
        return prod - sum
