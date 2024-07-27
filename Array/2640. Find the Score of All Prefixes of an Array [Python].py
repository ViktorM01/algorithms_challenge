class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_pref, s_val = 0, 0
        lst = []
        for i in range(n):
            max_pref = max(max_pref, nums[i])
            s_val = s_val + max_pref + nums[i]
            lst.append(s_val)
        return lst
