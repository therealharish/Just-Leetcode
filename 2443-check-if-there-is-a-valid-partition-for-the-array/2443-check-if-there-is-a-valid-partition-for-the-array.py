class Solution1:
    def validPartition(self, nums: List[int]) -> bool:
        # TC = O(n)
        # SC = O(1)
        @cache
        def solve(i):
            if i == len(nums):
                return True
            res = False
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                res = res or solve(i+2)
            if i < len(nums)-2 and nums[i] == nums[i+1] == nums[i+2]:
                res = res or solve(i+3)
            if i < len(nums)-2 and nums[i]+1 == nums[i+1] == nums[i+2]-1:
                res = res or solve(i+3)
            return res
        
        
        return solve(0)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        # tabulation
        
        dp = [False for _ in range(len(nums))]
        n = len(nums)
        if n >= 2 and nums[n-1]==nums[n-2]:
            dp[n-2] = True
        if n >= 3 and nums[n-1] == nums[n-2] == nums[n-3]:
            dp[n-3] = True
        if n >= 3 and nums[n-1]-1 == nums[n-2] == nums[n-3]+1:
            dp[n-3] = True
            
        for i in range(n-4, -1, -1):
            if nums[i] == nums[i+1]:
                dp[i] = dp[i+2]
            if nums[i] == nums[i+1] == nums[i+2]:
                dp[i] = dp[i] or dp[i+3]
            if nums[i]+1 == nums[i+1] == nums[i+2]-1:
                dp[i] = dp[i] or dp[i+3]
            # print(i, dp)
                
        return dp[0]