class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = list(), list()
        for i in range(len(nums)):
            if nums[i] > 0: 
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        lst = []
        for i in zip(pos, neg):
            lst.extend(list(i))
        return lst
