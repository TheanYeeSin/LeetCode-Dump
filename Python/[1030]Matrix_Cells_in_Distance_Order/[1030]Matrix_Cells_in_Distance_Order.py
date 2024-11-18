# Your Python code goes here.
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        all_cells = [[r, c] for r in range(rows) for c in range(cols)]

        all_cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return all_cells
