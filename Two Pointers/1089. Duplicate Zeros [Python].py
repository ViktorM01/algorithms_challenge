class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        cnt = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + cnt < n:
                arr[i + cnt] = arr[i]
            if arr[i] == 0:
                cnt -= 1
                if i + cnt < n:
                    arr[i + cnt] = 0
