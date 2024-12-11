# Your Python code goes here.
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_pairs = {}
        total = 0
        for domino in dominoes:
            pair = tuple(sorted(domino))
            if pair in domino_pairs:
                domino_pairs[pair] += 1
            else:
                domino_pairs[pair] = 1

        for value in domino_pairs.values():
            if value > 1:
                total += (value * (value - 1)) / 2
        return int(total)
