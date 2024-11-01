class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        median = nums[n//2]
        for i in range(len(nums)):
            ans += abs(nums[i] - median)
        return ans
