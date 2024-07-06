class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rnd = time // (n - 1)
        return (time % (n - 1) + 1) if rnd % 2 == 0 else (n - time % (n - 1))
