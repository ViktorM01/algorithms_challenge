class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rs = float('inf')
        dp = [n*[-1] for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                fl = float('inf')
                for t in range(n):
                    if j != t:
                        fl = min(fl, grid[i][j] + dp[i-1][t])
                dp[i][j] = fl
        
        for j in range(n):
            rs = min(rs, dp[n-1][j])

        return rs
