class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        flag = True
        n2 = len(nums2)
        for i in range(len(nums1)):
            bound2 = nums2.index(nums1[i])
            for j in range(bound2, n2):
                print(i, j)
                if nums2[j] > nums2[bound2]:
                    flag = False
                    lst.append(nums2[j])
                    break
            if flag:
                lst.append(-1)
            flag = True``
        return lst
            
