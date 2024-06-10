class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        lst_sort = heights.copy()
        lst_sort.sort()
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != lst_sort[i]:
                cnt += 1
        return cnt
