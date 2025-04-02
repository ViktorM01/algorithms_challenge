class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, max_dif, max_val = 0, 0, 0

        for k in nums:
            ans = max(ans, k * max_dif)
            max_dif = max(max_dif, max_val - k)
            max_val = max(max_val, k)

        return ans
