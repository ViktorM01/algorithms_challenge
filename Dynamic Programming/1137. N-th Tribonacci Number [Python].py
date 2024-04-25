class Solution:
    def tribonacci(self, n: int) -> int:
        lst = [0, 1, 1]
        if n <= 2: 
            return lst[n]
        else:
            while n >= len(lst):
                lst.append(sum(lst[-3:]))
            return lst[-1]
