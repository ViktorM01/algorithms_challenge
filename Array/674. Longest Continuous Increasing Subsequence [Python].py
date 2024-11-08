class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        max_cnt, cur_cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_cnt += 1
                max_cnt = max(max_cnt, cur_cnt)
            else:
                cur_cnt = 1
            
        return max_cnt
