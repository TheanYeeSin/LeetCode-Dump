# Your Python code goes here.
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return (primes := (2, 3, 5, 7, 11, 13, 17, 19)) and sum(
            (x.bit_count() in primes) for x in range(left, right + 1)
        )
