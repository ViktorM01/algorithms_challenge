class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in logs:
            if i == "./":
                pass
            elif i == "../":
                ans = max(ans-1, 0)
            else:
                ans += 1
        return ans
