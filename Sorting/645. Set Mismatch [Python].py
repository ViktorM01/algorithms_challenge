class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for n in nums:
            count[n - 1] += 1
        
        return [count.index(2) + 1, count.index(0) + 1]
