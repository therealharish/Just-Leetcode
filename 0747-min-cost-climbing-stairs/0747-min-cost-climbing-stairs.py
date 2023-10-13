class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]
        dp = {}
        def climb(n):
            if n == 0:
                dp[0] = cost[0]
                return cost[0]
            if n == 1:
                dp[1] = cost[1]
                return cost[1]
            if n in dp:
                return dp[n]
            dp[n] = min(climb(n-1), climb(n-2)) + cost[n]
            return dp[n]
        return climb(len(cost)-1)

# aakash sir's idea
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def climb(n):
            if n <= 1:
                return 0 
            if n in dp:
                return dp[n]
            leftPart = cost[n-1] + climb(n-1)
            rightPart = cost[n-2] + climb(n-2)
            dp[n] = min(leftPart, rightPart)
            return dp[n]
        return climb(len(cost))
    
# 7/4/23
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
        
