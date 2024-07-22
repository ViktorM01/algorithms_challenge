class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        for i in range(1, min_len + 1):
            prefix = strs[0][:i]
            ok = True
            for j in range(len(strs)):
                if prefix != strs[j][:i]:
                    ok = False
                    break
            
            if ok:
                ans = prefix
            else:
                break
        return ans
