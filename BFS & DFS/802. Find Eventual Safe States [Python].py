class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = set()
        ans = []
        lst = [0] * n

        def dfs(i):
            if (lst[i] == 1) or (len(graph[i]) == 0):
                return True
            elif (lst[i] == -1) or (i in visited):
                return False

            visited.add(i)
            for next_graph in graph[i]:
                if not dfs(next_graph):
                    lst[i] = -1
                    return False

            lst[i] = 1
            return True
        
        for i in range(n):
            if dfs(i):
                ans.append(i)
        
        return ans
