class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            lst.extend([int(d) for d in str(i)])
        return lst
