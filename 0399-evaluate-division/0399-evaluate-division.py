class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)
        for i in range(len(equations)):
            src, dst = equations[i]
            adj[src].append((dst, values[i]))
            adj[dst].append((src, 1/values[i]))

        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            q = deque()
            visited = set()
            q.append((src, 1))
            visited.add(src)
            while q:
                node, w = q.popleft()
                if node == dst:
                    return w
                for nbr, weight in adj[node]:
                    if nbr not in visited:
                        q.append((nbr, w * weight))
                        visited.add(nbr)
            return -1

        ans = []
        for src, dst in queries:
            ans.append(bfs(src, dst))
        return ans