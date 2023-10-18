class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        adj = {i:[] for i in range(1, n+1)}
        
        for src, dst in relations:
            adj[src].append(dst)
            
        indegree = {i:0 for i in range(1, n+1)}
        for src, dst in relations:
            indegree[dst] += 1
            
        
        courseTime = {i:0 for i in range(1, n+1)}
        
        q = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
                courseTime[i] = time[i-1]
        
        while q:
            curr = q.popleft()
            for dst in adj[curr]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)
                courseTime[dst] = max(courseTime[dst],courseTime[curr] + time[dst-1])
                # print(courseTime)
        
        if len(courseTime) != n:
            return -1
        else:
            return max(courseTime.values())