class Solution:
    def validPartition(self, nums: List[int]) -> bool:

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