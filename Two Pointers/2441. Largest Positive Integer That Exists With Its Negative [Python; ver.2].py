class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        max_k = float('-inf')
        while l < r:
            if nums[l] + nums[r] == 0:
                max_k = max(max_k, nums[r])
                l += 1
                r -= 1
            if nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1
        return max_k if max_k != float('-inf') else -1
