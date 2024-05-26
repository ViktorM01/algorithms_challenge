class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
         lst = zip(names, heights)
         lst = sorted(lst, key=lambda x: x[1], reverse=True)
         return [i[0] for i in lst]
