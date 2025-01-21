class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = float('inf')
        row1_sum, row2_sum = sum(grid[0]), 0

        for i in range(len(grid[0])):
            row1_sum -= grid[0][i]
            ans = min(ans, max(row1_sum, row2_sum))
            row2_sum += grid[1][i]
            
        return ans
