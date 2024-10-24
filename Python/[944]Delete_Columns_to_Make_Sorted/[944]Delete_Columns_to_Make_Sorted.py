# Your Python code goes here.
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c = []
        for i in range(len(strs) - 1):
            for j in range(len(strs[0])):
                if strs[i][j] > strs[i + 1][j]:
                    c.append(j)
        return len(set(c))
