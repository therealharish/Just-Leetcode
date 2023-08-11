class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        @cache
        def solve(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0
            res = solve(i, amount-coins[i]) + solve(i+1, amount)
            return res
        
        return solve(0, amount)
    
    