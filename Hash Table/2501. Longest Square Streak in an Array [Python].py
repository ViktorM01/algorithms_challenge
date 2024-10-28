class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = -1 
        dct_ = {}

        nums.sort()

        for num in nums:
            sqrt = int(num ** (1/2))
            if sqrt*sqrt == num and sqrt in dct_:
                dct_[num] = dct_[sqrt] + 1
                ans = max(ans, dct_[num])
            else:
                dct_[num] = 1
        return ans 
            
