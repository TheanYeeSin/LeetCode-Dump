# Your Python code goes here.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        n1 = 1
        n2 = 2
        i = 3
        while i <= n:
            next = n1
            n1 = n2
            n2 = next + n2
            i += 1
        return n2

        # Recursion approach

        # if n == 0 or n == 1:
        #     return 1
        # ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # return ans
