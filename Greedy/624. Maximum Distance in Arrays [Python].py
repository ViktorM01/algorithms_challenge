class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_, max_ = arrays[0][0], arrays[0][-1]
        max_dist = 0

        for i in range(1, len(arrays)):
            max_dist = max(max_dist, abs(arrays[i][-1] - min_), abs(max_ - arrays[i][0]))
            min_ = min(min_, arrays[i][0])
            max_ = max(max_, arrays[i][-1])

        return max_dist
