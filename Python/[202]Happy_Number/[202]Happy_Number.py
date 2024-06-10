# Your Python code goes here.
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        total = 0
        used = []
        while total != 1:
            total = 0
            for num in n:
                total += int(num) * int(num)
            n = str(total)
            if total in used:
                return False
            else:
                used.append(total)

        return True
