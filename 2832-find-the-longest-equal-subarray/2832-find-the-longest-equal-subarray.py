class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        d={}
        maxi=0
        left=0
        for right in range(len(nums)):
            if nums[right] in d:
                d[nums[right]]+=1
            else:
                d[nums[right]] = 1
            maxi=max(maxi,d[nums[right]])
            while right-left+1-maxi>k:
                d[nums[left]]-=1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left+=1
        return maxi