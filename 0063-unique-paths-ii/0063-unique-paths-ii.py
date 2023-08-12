#memoization
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {}
        if(obstacleGrid[m-1][n-1]==1):
            return 0
        def recur(r, c):
            if(r>m-1 or c>n-1):
                dp[(r, c)] = 0
                return 0
            if(obstacleGrid[r][c]==1):
                dp[(r, c)] = 0
                return 0
            if(r==m-1 and c==n-1):
                dp[(r, c)] = 1
                return 1
            if((r,c) in dp):
                return dp[(r,c)]
            dp[(r,c)] = recur(r+1, c) + recur(r, c+1)
            return dp[(r, c)]
        
        ans = recur(0, 0)
        return ans
        
        
# tabulation
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if(obstacleGrid[0][0] or obstacleGrid[m-1][n-1]):
            return 0
        obstacleGrid[0][0] = 1
        for r in range(m):
            for c in range(n):
                if(r==0 and c==0):
                    continue
                elif(obstacleGrid[r][c]==1):
                    obstacleGrid[r][c] = 0
                elif(r==0 and c!=0):
                    obstacleGrid[r][c] = obstacleGrid[r][c-1]
                elif(r!=0 and c==0):
                    obstacleGrid[r][c] = obstacleGrid[r-1][c]
                else:
                    obstacleGrid[r][c] = obstacleGrid[r][c-1]+obstacleGrid[r-1][c]
        return obstacleGrid[m-1][n-1]
                
# recursion - o(mn) time and O(mn) space
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if(obstacleGrid[0][0] or obstacleGrid[row-1][col-1]):
            return 0
        @lru_cache
        def solve(i, j):
            if i == row-1 and j == col - 1:
                return 1
            if i>=row or j>=col:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            return solve(i+1, j) + solve(i, j+1)
        return solve(0, 0)
    
# tabulatioon         
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if(obstacleGrid[0][0] or obstacleGrid[row-1][col-1]):
            return 0
        
        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        
        dp[0][1] = 1
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row][col]
        