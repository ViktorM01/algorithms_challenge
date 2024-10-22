class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, max_len, zeroes = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            max_len = max(max_len, r - l)

        return max_len
