class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        i, sum_max = 0, 0
        print(happiness)

        while k > 0:
            happiness[i] = max(happiness[i] - i, 0)
            sum_max += happiness[i]
            i += 1
            k -= 1

        return sum_max
