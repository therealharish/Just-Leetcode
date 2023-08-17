class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        
        q = deque()
        visited = set()
        
        for i in range(row):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][col - 1] == 'O':
                q.append((i, col - 1))
        
        for j in range(col):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[row - 1][j] == 'O':
                q.append((row - 1, j))
            
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while(q):
            
            x, y = q.popleft()
            if x < 0 or x >= row or y < 0 or y >= col or (x, y) in visited or board[x][y] == 'X':
                continue
            visited.add((x, y))
            board[x][y] = '1'
            for dx, dy in directions:
                q.append((x + dx, y + dy))
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'
        
        return board
                
            