class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        rev_lst = []

        for n in nums:
            rev_lst.append(nums[n])

        return rev_lst
