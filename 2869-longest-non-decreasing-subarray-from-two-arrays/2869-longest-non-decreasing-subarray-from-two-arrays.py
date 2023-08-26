class Solution:
    def maxNonDecreasingLength(self, A, B):
        dp, result = [1,1], 1
        for i in range(1, len(A)):
            dp2 = [1,1]
            if A[i] >= A[i - 1]: dp2[0] = dp[0] + 1
            if A[i] >= B[i - 1]: dp2[0] = max(dp2[0], dp[1] + 1)
            if B[i] >= A[i - 1]: dp2[1] = dp[0] + 1
            if B[i] >= B[i - 1]: dp2[1] = max(dp2[1], dp[1] + 1)                                
            result = max(result,  max(dp2))          
            dp = dp2
        return result