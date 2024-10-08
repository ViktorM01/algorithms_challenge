class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, cur_count = 0, 0
        for i in nums:
            if i == 1:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count = 0
        return max_count
