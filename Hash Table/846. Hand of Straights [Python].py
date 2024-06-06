class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        s_keys = sorted(count.keys())
        
        for k in s_keys:
            if count[k] > 0:
                s_count = count[k]
                for i in range(k, k + groupSize):
                    if count[i] < s_count:
                        return False
                    count[i] -= s_count
        return True
