class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l, max_len = 0, 0 
        nums.sort()
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                max_len = max(max_len, r - l + 1)
        return max_len
