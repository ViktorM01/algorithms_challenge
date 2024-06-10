class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        l = sum((map(int, list(''.join(list(map(str, nums)))))))
        return abs(sum(nums)-l)
