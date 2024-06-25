class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        if len(n) < 3:
            return max(nums)
        n = list(n)
        n.sort()
        return n[-3]
