class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_ = {}
        for index, key in enumerate(nums):
            if key in dict_ and abs(index - dict_[key]) <= k:
                return True
            dict_[key] = index
        return False
