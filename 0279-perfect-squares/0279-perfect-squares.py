class Solution:
    def numSquares(self, n: int) -> int:

        @cache
        def solve(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            i = 1
            res = float('inf')
            while (i*i <= n):
                res = min(res, 1 + solve(n-(i*i)))
                i += 1
            return res

        return solve(n)