class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        s = sum(cost)
        dp = [s for _ in range(n+1)]
        # dp[t] is min cost of when taking exactly t time
        for i in range(n):
            time[i] += 1 # so that we just need to minimize cost where total time >= n
        dp[0] = 0
        for i in range(n):
            for x in range(n-1,-1,-1):
                y = min(x+time[i],n) 
                # If painting index is greater than n, we view it as n
                dp[y] = min(dp[y],dp[x]+cost[i])
        return dp[-1] 