class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct_ = {key: nums.count(key) for key in set(nums)}
        return max(dct_, key=dct_.get)
