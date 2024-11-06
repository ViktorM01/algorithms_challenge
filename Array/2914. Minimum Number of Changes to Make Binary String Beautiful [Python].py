class Solution:
    def minChanges(self, s: str) -> int:
        min_change, idx = 0, 0
        while idx < len(s) - 1:
            if s[idx] != s[idx+1]:
                min_change += 1
            idx += 2
        return min_change
      
