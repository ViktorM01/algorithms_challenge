class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        t_wait = customers[0][1]
        f_prev = customers[0][0] + customers[0][1]
        
        for i in range(1, n):
            time = customers[i]
            arrive = time[0]

            start = max(arrive, f_prev)
            end = start + time[1]
            f_prev = end
            t_wait += end - arrive

        return t_wait / n
