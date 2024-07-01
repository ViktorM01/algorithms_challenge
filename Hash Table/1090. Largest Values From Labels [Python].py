class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        use_lim = {}
        val = 0
        zp = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)
        for i in zp:
            if numWanted == 0:
                return val
            if i[1] not in use_lim or use_lim[i[1]] < useLimit:
                val += i[0]
                numWanted -= 1
                if i[1] not in use_lim:
                    use_lim[i[1]] = 1
                else:
                    use_lim[i[1]] += 1
        return val
