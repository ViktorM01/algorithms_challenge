class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = [0] * len(nums)
        l, r = 0, len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if l <= r:
                if abs(nums[l]) >= abs(nums[r]):
                    lst[i] = nums[l]**2
                    l += 1
                else:
                    lst[i] = nums[r]**2
                    r -= 1
        return lst
