# recursion
class Solution1:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recur(pos):
            if(pos>=len(nums)):
                memo[pos] = 0
                return 0
            if pos in memo:
                return memo[pos]
            memo[pos] = max(nums[pos]+recur(pos+2), recur(pos+1))
            return memo[pos]
        return recur(0)

# tabulation
class Solution2:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        dp[len(nums)-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])
        return dp[0]

#include exclude principle
class Solution3:
    def rob(self, nums: List[int]) -> int:
        include = nums[0]
        exclude = 0
        for i in range(1, len(nums)):
            nextInclude = exclude+nums[i]
            nextExclude = max(include, exclude)
            include = nextInclude
            exclude = nextExclude
        return max(include, exclude)


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def solve(pos):
            if pos >= len(nums):
                return 0
            return max(nums[pos] + solve(pos + 2), solve(pos + 1))
        return solve(0)   