class Solution:

    def bin_search(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            if nums[l] + nums[r] <= k:
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.bin_search(nums, upper) - self.bin_search(nums, lower - 1)
