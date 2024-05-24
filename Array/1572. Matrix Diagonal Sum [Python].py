class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        f = 0
        for i in range(n):
            f += mat[i][i] + mat[i][n-1-i]
        if n % 2 == 1:
            f -= mat[n // 2][n // 2]
        return f
