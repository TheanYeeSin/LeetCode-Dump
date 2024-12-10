# Your Python code goes here.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        sorted_array = []
        for num in arr2:
            if num in count:
                sorted_array.extend([num] * count[num])
                del count[num]

        remaining = sorted([num for num in count.keys() for _ in range(count[num])])
        sorted_array.extend(remaining)

        return sorted_array
