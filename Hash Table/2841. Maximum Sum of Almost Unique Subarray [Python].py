class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        dict_ = {}    
        sum_ = 0
        ans = 0
        for i in range(k):
            if nums[i] in dict_:
                dict_[nums[i]] += 1
            else:
                dict_[nums[i]] = 1
            sum_ += nums[i]

        if len(dict_) >= m:
            ans = sum_

        for i in range(k, len(nums)):
            dict_[nums[i - k]] -= 1
            sum_ -= nums[i - k]
            if dict_[nums[i - k]] == 0:
                del dict_[nums[i - k]]

            if nums[i] in dict_:
                dict_[nums[i]] += 1
            else: 
                dict_[nums[i]] = 1

            sum_ += nums[i]

            if len(dict_) >= m:
                ans = max(ans, sum_)
            
        return ans
