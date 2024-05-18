# Your Python code goes here.
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return 0

        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        elif numRows > 2:
            final = [[1], [1, 1]]
            temp = []
            for i in range(0, numRows - 2):
                temp = [1]
                for j in range(0, len(final[-1]) - 1):

                    temp.append(final[-1][j] + final[-1][j + 1])

                temp.append(1)
                final.append(temp)

        return final
