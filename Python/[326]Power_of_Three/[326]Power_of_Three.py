# Your Python code goes here.
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        res = round(math.log(n, 3))
        return 3**res == n
