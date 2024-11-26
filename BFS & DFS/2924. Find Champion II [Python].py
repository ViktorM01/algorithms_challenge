class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        pretendents = [True] * n
        
        for win, lose in edges:
            pretendents[lose] = False
        
        champ, champ_numb = -1, 0

        for team in range(n):
            if pretendents[team]:
                champ = team
                champ_numb += 1
        
        if champ_numb == 1:
            return champ

        return -1
