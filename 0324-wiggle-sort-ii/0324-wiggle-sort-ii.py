class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = (len(nums)+1)//2
        left , right = nums[:mid][::-1] , nums[mid:][::-1]
        l , r = 0 , 0
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = left[l]
                l+=1
            else:
                nums[i] = right[r]
                r+=1
        return nums