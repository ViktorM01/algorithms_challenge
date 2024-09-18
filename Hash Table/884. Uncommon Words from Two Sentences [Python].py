class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst = s1.split() + s2.split()
        dict_ = {key: lst.count(key) for key in set(lst)}
        return [key for key, val in dict_.items() if val == 1]
