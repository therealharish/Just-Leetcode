class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]
        
        prefix[0] = 1
        suffix[len(nums)-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans