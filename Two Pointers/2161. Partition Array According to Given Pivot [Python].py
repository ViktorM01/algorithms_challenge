class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lst1, lst2, lst3 = [], [], []
        for el in nums:
            if el < pivot: 
                lst1.append(el)
            elif el == pivot:
                lst2.append(el)
            elif el > pivot:
                lst3.append(el)
        return lst1 + lst2 + lst3
