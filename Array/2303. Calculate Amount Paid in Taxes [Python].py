class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax, prev = 0, 0
        for up, p in brackets:
            if income >= up:
                tax += (up - prev) * p / 100
                prev = up
            else:
                tax += (income - prev) * p / 100
                return tax
        return tax
