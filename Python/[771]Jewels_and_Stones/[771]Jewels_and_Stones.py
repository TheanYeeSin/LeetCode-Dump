# Your Python code goes here.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in set(jewels))
