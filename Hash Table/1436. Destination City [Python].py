class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {i[0]: i[1] for i in paths}
        k = [val for val in dic.values() if val not in dic.keys()][0]
        return k
