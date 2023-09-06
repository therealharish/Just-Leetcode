class Solution1:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def solve(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = 0
            ways += solve(i+1)
            if i+1 < len(s) and int(s[i:i+2])>=1 and int(s[i:i+2])<=k:
                ways += solve(i+2)
            return ways
        
        return solve(0)

#tabulation        
class Solution2:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        dp = [0 for i in range(n+1)]
        dp[n] = 1
        
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue 
            ways = dp[i+1]
            if i+1 < n and int(s[i:i+2])>=1 and int(s[i:i+2])<=26:
                ways += dp[i+2]
            dp[i] = ways
        
        return dp[0]

# practise
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        @cache
        def solve(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            ways = 0
            ways += solve(i+1)
            if i + 1 < n and int(s[i:i+2])>=1 and int(s[i:i+2])<=26:
                ways += solve(i + 2)
            return ways

        return solve(0) 
