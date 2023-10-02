class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        ans=0
        v=0
        for i in range(len(nums)):
            if nums[i]==mx:
                v+=1
                ans=max(ans,v)
            else:
                v=0
        return ans
                