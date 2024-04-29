class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        fin_xor = 0
        for elem in nums:
            fin_xor = fin_xor ^ elem

        c = 0
        
        while k or fin_xor:
            if (k % 2) != (fin_xor % 2):
                c += 1
            k //= 2
            fin_xor //= 2

        return c
