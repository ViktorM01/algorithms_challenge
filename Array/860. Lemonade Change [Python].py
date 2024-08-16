class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = [0, 0]
        for i in bills:
            if i == 5:
                cnt[0] += 1
            if i == 10:
                cnt[0] -= 1
                cnt[1] += 1
                if cnt[0] < 0:
                    return False
            if i == 20:
                if cnt[1] > 0 and cnt[0] > 0:
                    cnt[0] -= 1
                    cnt[1] -= 1
                elif cnt[0] > 2:
                    cnt[0] -= 3
                else:
                    return False
        return True
