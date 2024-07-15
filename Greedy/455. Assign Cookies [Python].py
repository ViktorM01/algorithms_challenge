class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        g_p, s_p = 0, 0 
        while s_p < len(s) and g_p < len(g):
            if s[s_p] >= g[g_p]:
                g_p += 1
                ans += 1
            s_p += 1
        return ans
