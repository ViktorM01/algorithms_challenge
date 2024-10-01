class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_len = min(len(s1), len(s2), len(s3))
        cnt = len(s1) + len(s2) + len(s3)
        l = 0

        if s1[0] != s2[0] or s1[0] != s3[0] or s2[0] != s3[0]:
            return -1

        while l < min_len:
            if s1[l] == s2[l] == s3[l]:
                cnt -= 3
            else: 
                break
            l += 1

        return cnt
            
