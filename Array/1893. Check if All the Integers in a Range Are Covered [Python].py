class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n = len(ranges)
        pref_sum = [0] * 52
        for el in ranges:
            start, end = el[0], el[1]
            pref_sum[start] += 1
            pref_sum[end+1] -= 1

        for i in range(1, len(pref_sum)):
            pref_sum[i] += pref_sum[i-1]
        
        for i in range(left, right+1):
            if pref_sum[i] < 1:
                return False
                
        return True
