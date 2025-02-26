class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum, sum = 0, 0, 0
        for el in nums:
            sum += el
            max_sum = max(max_sum, sum)
            min_sum = min(min_sum, sum)
        return max_sum - min_sum
