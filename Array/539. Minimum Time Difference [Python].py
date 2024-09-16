class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) != len(set(timePoints)):
            return 0

        time_in = []
        for i in timePoints:
            time_h, time_m = map(int, i.split(':'))
            time_in.append(60*time_h + time_m)
        
        min_diff = float('inf')
        time_in.sort()
        for i in range(1, len(time_in)):
            min_diff = min(min_diff, time_in[i] - time_in[i-1])

        return min(min_diff, 1440 + time_in[0] - time_in[-1])
