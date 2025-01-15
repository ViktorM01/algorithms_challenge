class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b_num1, b_num2 = bin(num1).count('1'), bin(num2).count('1')
        ans = num1
        for i in range(32):
            if b_num1 > b_num2 and (1 << i) & num1 > 0:
                ans ^= 1 << i
                b_num1 -= 1
            if b_num1 < b_num2 and (1 << i) & num1 == 0:
                ans ^= 1 << i
                b_num1 += 1
        return ans
