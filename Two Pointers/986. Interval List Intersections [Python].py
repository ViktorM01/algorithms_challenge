class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        N, M = len(firstList), len(secondList)
        i, j = 0, 0
        ans = []

        while i < N and j < M:
            head_1, tail_1 = firstList[i][0], firstList[i][1]
            head_2, tail_2 = secondList[j][0], secondList[j][1]

            head_max, tail_min = max(head_1, head_2), min(tail_1, tail_2)
            if head_max <= tail_min:
                ans.append([head_max, tail_min])

            if tail_1 < tail_2:
                i += 1
            else:
                j += 1
                
        return ans
