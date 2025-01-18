class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        minCost = [[float('inf')] * n for _ in range(m)]
        minCost[0][0] = 0
        
        deq = deque([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while deq:
            r, c = deq.popleft()

            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0
                
                if 0 <= nr < m and 0 <= nc < n and minCost[r][c] + cost < minCost[nr][nc]:
                    minCost[nr][nc] = minCost[r][c] + cost
                    
                    if cost == 1:
                        deq.append((nr, nc))
                    else:
                        deq.appendleft((nr, nc))

        return minCost[m - 1][n - 1]
        
