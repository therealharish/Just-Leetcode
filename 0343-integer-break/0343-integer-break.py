class Solution:
    def integerBreak(self, n: int) -> int:

        @cache
        def solve(num):
            if num == 1:
                return 1
            if n == num:
                res = 0
            else:
                res = num
            for i in range(1, num):
                val = solve(i) * solve(num-i)
                res = max(val, res)
            return res
        
        return solve(n)
        