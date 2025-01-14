# Your Python code goes here.
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 != 0:
            result.append(0)

        for i in range(n):
            if len(result) != n:
                result.append(-i - 1)
                result.append(i + 1)
        return result
