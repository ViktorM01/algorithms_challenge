class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        for i in nums:
            if i >= k:
                return count
            else:
                count += 1
