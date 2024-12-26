# Your Python code goes here.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for _, element in enumerate(arr):
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1

        set_count = set(counts.values())
        if len(counts) == len(set_count):
            return True
        return False
