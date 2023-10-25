class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(n, k):
            if n == 1 or k == 1:
                return 0
            prevRow = n-1
            elements = 2**(prevRow-1)
            if(k>elements):
                k = k-elements
                return 1-solve(n-1, k)
            else:
                return solve(n-1, k)
        return solve(n, k)