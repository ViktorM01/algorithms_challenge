class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for end in range(len(nums)-1):
            if nums[end] + nums[end+1] in seen:
                return True
            seen.add(nums[end] + nums[end+1])
        return False
