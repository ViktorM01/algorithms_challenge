class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        n = len(grid[0])
        lst = [0] * n

        for i in range(len(grid)):
            for j in range(n):
                if len(str(grid[i][j])) > lst[j]:
                    lst[j] = len(str(grid[i][j]))

        return lst
