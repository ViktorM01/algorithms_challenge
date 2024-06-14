class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {key: nums.count(key) for key in set(nums)}
        return sum([key for key, i in dic.items() if i == 1])
