class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_points = sorted(i[0] for i in intervals)
        end_points = sorted(i[1] for i in intervals)
        end_p, groups = 0, 0

        for start in start_points:
            if start > end_points[end_p]:
                end_p += 1
            else:
                groups += 1
        
        return groups
