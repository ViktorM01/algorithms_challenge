class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        dct_ = {}
        for n in range(len(arr)):
            if arr[n] in dct_:
                dct_[arr[n]] += 1
            else:
                dct_[arr[n]] = 1
            
        for n in dct_:
            if dct_[n] == 1:
                k -= 1
            if k == 0:
                return(n)
        
        return ''
