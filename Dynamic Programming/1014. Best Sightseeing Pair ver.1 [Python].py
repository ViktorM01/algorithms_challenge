class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        suffix_dp, max_ans = 0, 0
        # suffix_dp = i + values[i]
        # max_ans = suffix_dp + values[i] - i

        for idx, el in enumerate(values):
            max_ans = max(max_ans, suffix_dp + el - idx)
            suffix_dp = max(suffix_dp, el + idx)
         
        return max_ans
