class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        for l in nums:
            if l - 1 not in nums:
                r = l + 1
                while r in seen:
                    r += 1
                ans = max(ans, r - l)
        return ans
