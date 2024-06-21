class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        sect = set(nums1) & set(nums2)
        if sect:
            return min(sect)
        d1, d2 = min(nums1), min(nums2)
        return int(str(d1) + str(d2)) if d1 < d2 else int(str(d2) + str(d1))
