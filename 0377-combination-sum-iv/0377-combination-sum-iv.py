class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(rem):
            if rem in memo:
                return memo[rem]
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            res = 0
            for i in nums:
                res += dp(rem-i)
            memo[rem] = res
            return res
        return dp(target)