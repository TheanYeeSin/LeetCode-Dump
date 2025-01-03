# Your Python code goes here.
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for index in indices:
            a = index[0]  # row
            b = index[1]  # col
            for i in range(n):
                matrix[a][i] += 1

            for j in range(m):
                matrix[j][b] += 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2:
                    count += 1
        return count
