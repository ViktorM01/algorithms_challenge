class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num), reverse = True)
        return int(num[0]) + int(num[1]) + (int(num[2]) + int(num[3]))* 10
