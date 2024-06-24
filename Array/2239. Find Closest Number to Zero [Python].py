class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = min(abs(x) for x in nums)
        return ans if ans in nums else -ans
