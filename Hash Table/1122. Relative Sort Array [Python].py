class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {key: arr1.count(key) for key in set(arr1)}
        lst = []
        for el in arr2:
            lst.extend([el] * dic[el])
        lst.extend(sorted([i for i in arr1 if i not in set(arr2)]))
        return lst
