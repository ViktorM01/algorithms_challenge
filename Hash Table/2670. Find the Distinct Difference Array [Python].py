class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return lst
