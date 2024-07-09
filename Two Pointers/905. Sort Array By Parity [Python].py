class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, 0
        n = len(nums)
        while p1 < n:
            if nums[p1] % 2 != 0:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
        return nums
