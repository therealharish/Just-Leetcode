class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp=[1 for i in range(len(pairs))]
        dp[0]=1
        for i in range(1,len(pairs)):
            for j in range(i-1,-1,-1):
                if pairs[i][0]>pairs[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp[len(pairs)-1]