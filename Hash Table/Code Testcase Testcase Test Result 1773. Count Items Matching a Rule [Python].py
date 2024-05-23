class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        d = {'type': 0, 'color': 1, 'name': 2}
        for i in items:
            if i[d.get(ruleKey)] == ruleValue:
                cnt += 1
        
        return cnt
