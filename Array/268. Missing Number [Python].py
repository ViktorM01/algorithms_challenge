class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp_s = len(nums) * (len(nums) + 1) // 2
        act_s = sum(nums)
        return exp_s - act_s
