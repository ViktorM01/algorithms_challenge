class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def find_bob_path():
            queue = deque([(bob, -1, [bob])])
            while queue:
                node, parent, path = queue.popleft()
                if node == 0:
                    return path
                for neighbor in graph[node]:
                    if neighbor != parent:
                        queue.append((neighbor, node, path + [neighbor]))
            return []

        bob_path = find_bob_path()
        bob_time = {node: i for i, node in enumerate(bob_path)}

        def dfs(node, parent, timestamp):
            if node in bob_time:
                if bob_time[node] < timestamp:
                    curr_score = 0
                elif bob_time[node] == timestamp:
                    curr_score = amount[node] // 2
                else:
                    curr_score = amount[node]
            else:
                curr_score = amount[node]
            
            if len(graph[node]) == 1 and node != 0:
                return curr_score

            max_score = -float('inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_score = max(max_score, dfs(neighbor, node, timestamp + 1))
            return curr_score + max_score

        return dfs(0, -1, 0)
