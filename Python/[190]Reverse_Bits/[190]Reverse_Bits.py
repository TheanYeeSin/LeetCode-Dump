# Your Python code goes here.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return self.f(n, 0, 0)

    def f(self, n, r, count):
        if n < 1:
            return r << (32 - count)
        return self.f(n >> 1, (r << 1) | (n & 1), count + 1)
