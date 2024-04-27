class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @functools.lru_cache(None)
        def dfs(ring, indx):
            if indx == len(key):
                return 0
            ans = float('inf')
            for i, r in enumerate(ring):
                if r == key[indx]:
                    min_rotates = min(i, len(ring)-i)
                    upd_ring = ring[i:] + ring[:i]
                    remain_rotates = dfs(upd_ring, indx+1)
                    ans = min(ans, min_rotates+remain_rotates)

            return ans
        return dfs(ring,0)+len(key)
