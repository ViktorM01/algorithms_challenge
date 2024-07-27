class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xor = n * [0]
        prefix_xor[0] = arr[0]

        for i in range(1, n):
            prefix_xor[i] = (prefix_xor[i-1] ^ arr[i])

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    left_xor = prefix_xor[j - 1]
                    if i - 1 >= 0:
                        left_xor ^= prefix_xor[i - 1]
                    right_xor = prefix_xor[k] ^ prefix_xor[j - 1]
                    if left_xor == right_xor:
                        ans += 1
        
        return ans
