class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dict_ = defaultdict(int)

        for row in matrix:
            row_find = tuple(row)

            if row[0]:
                row_find = tuple([0 if el else 1 for el in row])

            dict_[row_find] += 1

        return max(dict_.values())
