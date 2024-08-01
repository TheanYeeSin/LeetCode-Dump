# Your Python code goes here.
class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return a + b
        c = a + b
        for i in range(n - 2):
            a = b
            b = c
            c = a + b
        return c
