class Solution:
    def minimumSteps(self, s: str) -> int:
        black, ans = 0, 0
        for el in s:
            if el == '0':
                ans += black
            else:
                black += 1
        return ans
            
