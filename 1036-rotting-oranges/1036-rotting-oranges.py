class Solution1:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        q=deque([])
        freshpresent=False
        for i in range(row):
                for j in range(col):
                        if grid[i][j]==2:
                                q.append((i,j))
                        if grid[i][j]==1:
                                freshpresent=True
        mins=0
        tempq=deque([])
        if not freshpresent: return 0
        while q:
                # print(q,mins,grid)
                rotteni,rottenj=q.popleft()
                if (rotteni>0 and grid[rotteni-1][rottenj]==1):
                        grid[rotteni-1][rottenj]=2
                        tempq.append((rotteni-1,rottenj))
                if (rotteni<row-1 and grid[rotteni+1][rottenj]==1):
                        grid[rotteni+1][rottenj]=2
                        tempq.append((rotteni+1,rottenj))
                if (rottenj>0 and grid[rotteni][rottenj-1]==1):
                        grid[rotteni][rottenj-1]=2
                        tempq.append((rotteni,rottenj-1))
                if (rottenj<col-1 and grid[rotteni][rottenj+1]==1):
                        grid[rotteni][rottenj+1]=2
                        tempq.append((rotteni,rottenj+1))
                if not q:
                        q=deque(list(tempq)[::])
                        tempq.clear()
                        mins+=1
        for i in range(row):
                for j in range(col):
                        if grid[i][j]==1: return -1
        return mins-1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        q = deque()
        visited = set()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                        oranges += 1
        if not oranges:
                return 0
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0
        while q:
                for _ in range(len(q)):
                        r, c = q.popleft()
                        if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r, c) in visited:
                                continue
                        visited.add((r, c))
                        grid[r][c] = 2
                        for x, y in direction:
                                newR, newC = r + x, c + y
                                q.append((newR, newC))
                time += 1
        for i in range(row):
                for j in range(col):
                        if grid[i][j] == 1:
                                return -1
        return time - 2
                        
                        
                
                