class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] -= 1
        
        for i in range(len(nums)):
            while nums[i] != i and nums[i] != nums[nums[i]]:
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
            # print(nums)
                
        ans = []
        for i in range(len(nums)):
            if nums[i] != i:
                ans.append(nums[i] + 1)
                
        return ans