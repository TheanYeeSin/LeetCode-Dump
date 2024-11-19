# Your Python code goes here.
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a, b, c = points
        return (b[1] - a[1]) * (c[0] - b[0]) != (c[1] - b[1]) * (b[0] - a[0])
