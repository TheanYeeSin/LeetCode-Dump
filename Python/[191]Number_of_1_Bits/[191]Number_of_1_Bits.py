# Your Python code goes here.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(bin(n))
        ans = 0
        for c in s:
            if c == "1":
                ans += 1
        return ans
