# Your Python code goes here.
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        return (p := Counter([c for c in licensePlate.lower() if c.isalpha()])) and min(
            [w for w in words if Counter(w) >= p], key=len
        )
