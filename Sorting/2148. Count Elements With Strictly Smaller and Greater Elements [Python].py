class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_ab, min_ab = max(nums), min(nums)
        return max(0, len(nums) - nums.count(max_ab) - nums.count(min_ab))
