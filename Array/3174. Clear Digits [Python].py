class Solution:
    def clearDigits(self, s: str) -> str:
        cnt = 0
        s = list(s)
        for i, c in enumerate(s):
            if c.isdigit() and cnt > 0: 
                cnt -= 1
            else:
                s[cnt] = c
                cnt += 1
        s = s[:cnt] 
        return "".join(s)
        
        
