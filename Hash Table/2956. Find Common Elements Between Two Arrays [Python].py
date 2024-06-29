class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s_set = set(nums1) & set(nums2)
        s1, s2 = 0, 0 
        for n in nums1:
            if n in s_set:
                s1 += 1
        for n in nums2:
            if n in s_set:
                s2 += 1  

        return [s1, s2]     
