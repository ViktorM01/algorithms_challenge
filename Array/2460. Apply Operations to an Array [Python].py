class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        l, r = 0, 0
        while r < n:
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums
            
