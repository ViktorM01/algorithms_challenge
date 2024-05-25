class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {jew: stones.count(jew) for jew in set(jewels)}
        return sum([val for val in dic.values()])
