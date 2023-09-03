# Simple recursion without DP - Gives TLE 
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        def recur(r, c):
            if(r>m or c>n):
                return 0
            if(r==m-1 and c==n-1):
                return 1
            else:
                return recur(r+1, c)+recur(r, c+1)
        
        ans = recur(0,0)
        return ans

# recursion with memoization
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def recur(r, c):
            if(r>m or c>n):
                dp[(r,c)] = 0
                return 0
            if(r==m-1 and c==n-1):
                dp[(r,c)] = 1
                return 1
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = recur(r+1, c)+recur(r, c+1)
            return dp[(r,c)]
        
        ans = recur(0,0)
        return ans
    
# Tabulation
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i-1][j]+table[i][j-1]
        return table[m-1][n-1]

#Combinatrics
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m+n-2
        r = min(m-1, n-1)
        res = 1
        for i in range(1,r+1):
            res = (res*(N-r+i))/i
        return int(res)

#Permutation and combinations
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        southDirection = m-1
        eastDirection = n-1
        N = m+n-2
        r = min(southDirection, eastDirection)
        # r is essentially taking factorial NCR and keeping r to a minimum helps
        res = 1
        for i in range(1,r+1):
            res = (res*(N-r+i))/i
        return int(res)