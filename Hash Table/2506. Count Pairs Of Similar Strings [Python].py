class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        dct_ = {}

        for n in words:
            vec = [0] * 26
            for s in range(len(n)):
                vec[ord(n[s]) - ord('a')] = 1
                
            vec = tuple(vec)

            if vec in dct_:
                dct_[vec] += 1
            else:
                dct_[vec] = 1

        ans = 0

        for key in dct_:
            k = dct_[key]
            ans += (k-1) * k // 2

        return ans
