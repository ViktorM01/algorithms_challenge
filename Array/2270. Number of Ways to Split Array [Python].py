class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums)
        valid_splits = 0

        for i in range(len(nums) - 1):
            l_sum += nums[i]
            r_sum -= nums[i]
            if l_sum >= r_sum:
                valid_splits += 1

        return valid_splits
