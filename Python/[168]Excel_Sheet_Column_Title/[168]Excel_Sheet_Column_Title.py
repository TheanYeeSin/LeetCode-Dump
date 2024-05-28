# Your Python code goes here.
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        temp = columnNumber
        final = ""
        while temp:
            temp, remainder = divmod(temp - 1, 26)
            print(remainder)
            final += chr(65 + remainder)

        return final[::-1]
