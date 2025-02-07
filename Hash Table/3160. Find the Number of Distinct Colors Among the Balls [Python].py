class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        bal = {}
        col = defaultdict(int)
        res = []

        for key, value in queries:
            if key in bal:
                old_value = bal[key]
                col[old_value] -= 1
                if col[old_value] == 0:
                    del col[old_value]
            
            bal[key] = value
            col[value] += 1
            res.append(len(col))

        return res
