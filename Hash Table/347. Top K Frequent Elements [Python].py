class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct_ = {}
        lst = []
        for i in nums:
            if i not in dct_:
                dct_[i] = 1
            else:
                dct_[i] +=1 

        top_K = sorted(dct_.values(), reverse=True)[:k]
        
        for key, val in dct_.items():
            if val in top_K:
                lst.append(key)
        
        return lst
