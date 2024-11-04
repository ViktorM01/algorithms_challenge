class Solution:
    def compressedString(self, word: str) -> str:
        symb, cnt = word[0], 1
        ans = ''
        for i in range(1, len(word)):
            if symb == word[i] and cnt < 9:
                cnt += 1
            else:
                ans += str(cnt) + symb
                cnt = 1
                symb = word[i]
        ans += str(cnt) + symb
        return ans


