# Your Python code goes here.
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ll = []
        i = 0
        while i < len(s):
            left = i + 1
            while left < len(s) and s[i] == s[left]:
                left += 1
            if left - i - 1 >= 2:
                ll.append([i, left - 1])
                i = left - 1
            i += 1
        return ll
