class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        d = sum([int(d) for d in str(x)])
        return d if x % d == 0 else -1
