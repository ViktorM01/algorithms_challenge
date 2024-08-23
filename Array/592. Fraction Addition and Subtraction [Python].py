class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        nom, denom = 0, 1

        for i in range(0, len(nums), 2):
            num1, num2 = nums[i], nums[i+1]
            nom = nom * num2 + denom * num1
            denom *= num2
            # print(nom, denom)

        com_div = gcd(nom, denom)
        return f"{nom//com_div}/{denom//com_div}"
