class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        lst = []
        for i in range(0, len(nums)-1, 2):
            lst.append(nums[i+1])
            lst.append(nums[i])

        return lst
