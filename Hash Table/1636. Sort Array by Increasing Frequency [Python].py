class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dct_ = {key: nums.count(key) for key in set(nums)}
        nums.sort(key = lambda x: (dct_[x], x))
        return nums
