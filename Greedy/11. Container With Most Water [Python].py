class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0
        while l < r:
            max_vol = max((r - l) * min(height[l], height[r]), max_vol)
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1

        return max_vol
