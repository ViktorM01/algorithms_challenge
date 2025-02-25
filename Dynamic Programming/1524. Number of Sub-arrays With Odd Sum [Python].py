class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cnt, pref_sum, mod = 0, 0, 1_000_000_007
        for i in range(len(arr)):
            pref_sum += arr[i]
            cnt += pref_sum % 2
        cnt += (len(arr) - cnt) * cnt
        return cnt % mod
