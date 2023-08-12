class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        path_rem = [[[0]*k for _ in range(n)] for __ in range(m)]
        col1 = row1 = 0
        for i in range(m):
            col1 = (col1 + grid[i][0]) % k
            path_rem[i][0][col1] = 1
        for j in range(n):
            row1 = (row1 + grid[0][j]) % k
            path_rem[0][j][row1] = 1
        for i in range(1, m):
            for j in range(1, n):
                path_rem[i][j] = deque([left + up for left, up in zip(path_rem[i][j-1],path_rem[i-1][j])])
                path_rem[i][j].rotate(grid[i][j] % k)
        return path_rem[m-1][n-1][0] % (10 ** 9 + 7)