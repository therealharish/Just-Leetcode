class Solution:
    def numTrees(self, n: int) -> int:

        @cache
        def solve(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            s = 0
            for i in range(1, n+1):
                s += solve(i-1) * solve(n-i)
            return s
        
        return solve(n)

        