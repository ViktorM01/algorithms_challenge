class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        tries = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                tries += 1     
            if tries > 1:
                return False
        return True
