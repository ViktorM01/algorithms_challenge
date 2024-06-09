class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        pref_map = {0: 1}
        pref_sum = 0

        for n in nums:
            pref_sum += n
            mod = pref_sum % k
            if mod < 0:
                pass
            if mod in pref_map:
                cnt += pref_map[mod]
                pref_map[mod] += 1 
            else: 
                pref_map[mod] = 1
                
        return cnt
            
