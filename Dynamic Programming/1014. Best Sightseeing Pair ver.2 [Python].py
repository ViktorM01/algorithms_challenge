class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        suffix_arr = [0] * n
        suffix_arr[n - 1] = values[n - 1] - (n - 1)
        max_ans = float('-inf')

        for j in range(n - 2, -1, -1):
            suffix_arr[j] = max(suffix_arr[j + 1], values[j] - j)

        for i in range(n - 1):
            max_ans = max(max_ans, suffix_arr[i + 1] + i + values[i])
        
        return max_ans
         
