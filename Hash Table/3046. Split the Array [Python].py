class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dct_ = {}
        for num in nums:
            if num in dct_:
                dct_[num] += 1
            else:
                dct_[num] = 1

        return all(v <= 2 for v in dct_.values())
