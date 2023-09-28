class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        i = 0
        for j in range(len(nums)):
            curr = nums[j]
            if not curr & 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums