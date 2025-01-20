class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        position_dict = {mat[i][j]: (i, j) for i in range(rows) for j in range(cols)}
        
        cnt_rows = [cols] * rows
        cnt_cols = [rows] * cols

        for idx, val in enumerate(arr):
            row, col = position_dict[val]
            cnt_rows[row] -= 1
            cnt_cols[col] -= 1
            if (cnt_rows[row] == 0) or (cnt_cols[col] == 0):
                return idx
        return -1
