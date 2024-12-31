# Your Python code goes here.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count = 0

        for char in s:
            count += 1 if char == "R" else -1

            if count == 0:
                result += 1

        return result
