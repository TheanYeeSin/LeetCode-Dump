# Your Python code goes here.
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        res = round(math.log(n, 4))
        return 4**res == n
