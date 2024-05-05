# Your Python code goes here.
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x and (mid + 1) * (mid * 1) > x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return int(left - 1)
