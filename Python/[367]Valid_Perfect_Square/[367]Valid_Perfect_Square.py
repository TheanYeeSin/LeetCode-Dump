# Your Python code goes here.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while True:
            power_n = n * n
            next_power_n = (n + 1) * (n + 1)
            if power_n == num:
                return True
            elif power_n < num and next_power_n > num:
                return False
            n = n + 1
        return False
