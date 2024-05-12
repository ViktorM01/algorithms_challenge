class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i, j = 0, n
        ans = []

        while i <= n-1:
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        
        return ans
