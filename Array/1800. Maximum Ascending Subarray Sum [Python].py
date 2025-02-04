class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_cnt, max_cnt = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_cnt += nums[i]
            else:
                cur_cnt = nums[i]
            max_cnt = max(max_cnt, cur_cnt)
        return max_cnt
