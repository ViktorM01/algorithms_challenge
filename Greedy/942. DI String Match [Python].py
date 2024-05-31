class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0] * (len(s) + 1)
        cnt, high = 0, len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                ans[i] = cnt
                cnt += 1
            else: 
                ans[i] = high
                high -= 1
        ans[-1] = cnt
        return ans
