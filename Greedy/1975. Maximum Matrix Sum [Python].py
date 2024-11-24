class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg, min_val, sum_abs = 0, float('inf'), 0

        for row in matrix:
            for val in row:
                if val < 0:
                    neg += 1
                sum_abs += abs(val)
                min_val = min(min_val, abs(val))

        if neg % 2 == 1:
            sum_abs -= 2 * min_val

        return sum_abs
