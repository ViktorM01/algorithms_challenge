class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:           
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res
