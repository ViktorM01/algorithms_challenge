class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum_val = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    sum_val += 1

        return sum_val
