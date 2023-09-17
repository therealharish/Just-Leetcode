class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        finalState = (2**(len(graph)))-1
        
        q = deque()
        visited = set()
        for i in range(len(graph)):
            q.append((i, 1<<i))
            visited.add((i, 1<<i))

        dist = 0
        while(q):
            dist += 1
            # print(visited)
            for i in range(len(q)):
                currNode, currState = q.popleft()
                if currState == finalState:
                    return dist - 1
                for newNode in graph[currNode]:
                    newState = currState | (1 << newNode)
                    # print(newNode, newState)
                    if (newNode, newState) in visited:
                        continue
                    else:
                        q.append((newNode, newState))
                        visited.add((newNode, newState))

        
                


# [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]
            