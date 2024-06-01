class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frq = [0] * (len(nums) + 1)
        ans = []

        for i in nums:
            if frq[i] >= len(ans):
                ans.append([])
            ans[frq[i]].append(i)
            frq[i] += 1
        return ans

        
