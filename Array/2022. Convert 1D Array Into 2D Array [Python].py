class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        len_ = len(original)
        if m * n != len_:
            return []

        lst = []
        for i in range(m):
            lst.append(original[n*i:n*(i+1)])
        return lst
