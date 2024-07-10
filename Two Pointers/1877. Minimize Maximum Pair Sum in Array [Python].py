class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        maxi = float('-inf')

        while i < j:
            maxi = max(nums[i] + nums[j], maxi)
            i += 1
            j -= 1

        return maxi
