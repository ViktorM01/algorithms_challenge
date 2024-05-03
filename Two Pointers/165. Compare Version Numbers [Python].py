class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        f, s = 0, 0
        
        while (f < len(version1) or s < len(version2)):
            p1 = p2 = 0

            while (f < len(version1) and version1[f] != '.'):
                p1 = p1 * 10 + int(version1[f])
                f += 1
            while (s < len(version2) and version2[s] != '.'):
                p2 = p2 * 10 + int(version2[s])
                s += 1

            if p1 > p2:
                return 1
            if p1 < p2:
                return -1

            f, s = f + 1, s + 1

        return 0
            
