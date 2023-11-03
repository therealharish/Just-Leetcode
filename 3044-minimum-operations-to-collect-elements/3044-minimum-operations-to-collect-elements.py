class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        s = set({i for i in range(1, k+1)})
        i = len(nums)-1
        found = set()
        while(i >= 0):
            if nums[i] in s:
                found.add(nums[i])
            if len(found) == len(s):
                return len(nums) - i
            i -= 1
        return -1
                
