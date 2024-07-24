# Your Python code goes here.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        i = z
        count = 0
        while i > 0:
            count += i % 2
            i = i // 2
        return count
