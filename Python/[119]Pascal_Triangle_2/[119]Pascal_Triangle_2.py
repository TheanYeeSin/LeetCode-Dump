# Your Python code goes here.
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex > 1:

            final = [1, 1]
            for i in range(0, rowIndex - 1):
                temp = [1]
                for j in range(1, len(final)):
                    temp.append(final[j - 1] + final[j])
                temp.append(1)
                final = temp
            return final
