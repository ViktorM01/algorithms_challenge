class Solution:

    def dfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        if i >= self.m or j >= self.n or grid[i][j] == 0 or i < 0 or j < 0:
            return 0
        res = grid[i][j]
        grid[i][j] = 0
        res += self.dfs(i + 1, j, grid)
        res += self.dfs(i - 1, j, grid)
        res += self.dfs(i, j + 1, grid)
        res += self.dfs(i, j - 1, grid)
        return res
    
    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != 0:
                    ans = max(ans, self.dfs(i, j, grid))

        return ans
