class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(digit: int, target: int) -> int:
            if digit == target:
                return True
            if digit == 0:
                return target == 0
            for m in (10, 100, 1000):
                if partition(digit // m, target - digit % m):
                    return True
            return False

        return sum(digit for i in range(1, n + 1) if partition(digit := i * i, i))
