class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # possible size just 82 
        lst = [-1] * 82
        ans = -1

        for num in nums:
            digit_sum = sum(int(dd) for dd in str(num))
            if lst[digit_sum] != -1:
                ans = max(ans, num + lst[digit_sum])
            lst[digit_sum] = max(num, lst[digit_sum])
        return ans
