# Your Python code goes here.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        result = []
        minDiff = float("inf")

        for i in range(n - 1):
            minDiff = min(minDiff, arr[i + 1] - arr[i])

        for i in range(n - 1):
            if arr[i + 1] - arr[i] == minDiff:
                result.append([arr[i], arr[i + 1]])

        return result
