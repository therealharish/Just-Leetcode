class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row, col = len(mat), len(mat[0])
        
        q = deque()
        visited = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i, j))
                    
        ans = [[0 for _ in range(col)] for _ in range(row)]
        
        dist = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = [[0 for _ in range(col)] for _ in range(row)]
        while(q):
            
            for i in range(len(q)):
                x, y = q.popleft()
                if x < 0 or x >= row or y < 0 or y >= col or visited[x][y]:
                    continue
                ans[x][y] = dist
                visited[x][y] = 1
                for dx, dy in directions:
                    q.append((x + dx, y + dy))
            dist += 1

        return ans

            

                    
            
            