class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, prev = 0, -1

        for i, numb in enumerate(seats):
            if numb > 0:
                dist = i if prev == -1 else (i - prev) // 2
                res = max(res, dist)
                prev = i
            
        if not seats[i]:
            res = max(res, i - prev)

        return res
