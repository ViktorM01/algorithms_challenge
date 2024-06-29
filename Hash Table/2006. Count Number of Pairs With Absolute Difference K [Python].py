class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        freq = {}

        for n in nums:
            if n + k in freq:
                cnt += freq[n+k]
            if n - k in freq:
                cnt += freq[n-k]
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        return cnt
