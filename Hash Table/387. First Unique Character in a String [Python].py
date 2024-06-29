rewrite in C++ 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = []
        dct = {key: s.count(key) for key in set(s)}
        for key, val in dct.items():
            if val == 1: 
                lst.append(s.index(key))
        return min(lst) if len(lst) > 0 else -1
