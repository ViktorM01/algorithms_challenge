class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict_ = {}
        for el in nums:
            dict_[el] = 1

        R = 2 * (10 ** 5) + 10
        for i in range(1, R):
            if i in dict_:
                continue
            else:
                return i
