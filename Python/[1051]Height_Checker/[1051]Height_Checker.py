# Your Python code goes here.
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sortH = [x for x in heights]
        sortH.sort()
        ans = 0
        for i in range(len(heights)):
            if sortH[i] != heights[i]:
                ans += 1
        return ans
