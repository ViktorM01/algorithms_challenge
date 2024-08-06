class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1): 
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        ans = 0
        dict_ = {}

        for i in range(n + 1):
            prefix_sum[i] %= k
            if prefix_sum[i] in dict_:
                ans += dict_[prefix_sum[i]]
            
            if prefix_sum[i] in dict_:
                dict_[prefix_sum[i]] += 1
            else:
                dict_[prefix_sum[i]] = 1

        return ans
