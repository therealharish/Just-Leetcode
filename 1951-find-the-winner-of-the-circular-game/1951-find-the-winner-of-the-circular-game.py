class Solution:
    def solve(self,n,k):
        if n == 1:
            return 0
        return (self.solve(n-1,k) + k) % n
    def findTheWinner(self, n: int, k: int) -> int:
        return self.solve(n,k) + 1