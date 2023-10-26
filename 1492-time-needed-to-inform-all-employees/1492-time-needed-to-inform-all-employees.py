class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        adj = {i:[] for i in range(n)}

        for i in range(len(manager)):
            curr = manager[i]
            if curr == -1:
                continue
            adj[curr].append(i)
            
        visited =set()
        def dfs(node, parentTime):
            visited.add(node)
            informTime[node] += parentTime
            for child in adj[node]:
                if child not in visited:
                    dfs(child, informTime[node])

        dfs(headID, 0)
        return max(informTime)

            

