class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numb = ''
        sum_ = 0
        for i in range(len(s)):
            numb += str(ord(s[i]) - ord('a') + 1)
    
        while k > 0:
            numb = str(sum([int(i) for i in numb]))
            k -= 1
        
        return int(numb)
