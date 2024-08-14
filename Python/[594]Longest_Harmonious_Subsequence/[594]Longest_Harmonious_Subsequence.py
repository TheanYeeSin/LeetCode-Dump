# Your Python code goes here.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        ans = 0
        for c in count:
            if c + 1 in count:
                ans = max(ans, count[c] + count[c + 1])
        return ans
