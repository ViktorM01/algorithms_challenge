class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return next((v for v in nums1 if (i := bisect_left(nums2, v)) < len(nums2) and nums2[i]==v), -1)
