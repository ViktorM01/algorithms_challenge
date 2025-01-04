class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right_sum = [0] * 26
        left_sum = [0] * 26
        ans_set = set()

        for symb in s:
            right_sum[ord(symb) - ord('a')] += 1
        
        for i in range(len(s)):
            symb = ord(s[i]) - ord('a')
            right_sum[symb] -= 1
            for j in range(26):
                if left_sum[j] > 0 and right_sum[j] > 0:
                    ans_set.add(26 * symb + j)
            left_sum[symb] += 1
        
        return len(ans_set)
