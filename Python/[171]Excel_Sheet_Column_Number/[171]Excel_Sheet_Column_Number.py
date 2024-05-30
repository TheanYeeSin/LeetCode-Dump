# Your Python code goes here.
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        total = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            total += (ord(columnTitle[i]) - 64) * (26 ** (len(columnTitle) - (i + 1)))
        return total
