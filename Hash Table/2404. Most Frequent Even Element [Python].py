class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dct_ = {}
        for n in nums:
            if (n % 2 == 0):
                dct_[n] = dct_.get(n, 0) + 1

        if not dct_:
            return -1
        
        t = sorted(dct_.items(), key=lambda x: (-x[1], x[0]))
        return t[0][0]
