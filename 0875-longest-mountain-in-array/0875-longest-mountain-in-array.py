class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        if len(nums) == 3:
            if nums[0] < nums[1] > nums[2]: return 3
            else: return 0
        l = 0
        maxx = 0
        inn = False
        while l < len(nums) - 1:
            c = 0
            while nums[l] < nums[l+1]:
                l += 1
                c += 1
                if l == len(nums) - 1: break
            
            if l == len(nums) - 1: break
            if c > 0:
                while nums[l+1] < nums[l]:
                    # print(l,nums[l],nums[l+1],'innn')
                    l += 1
                    c += 1
                    inn = True
                    if l == len(nums) -1: break
                    
                # print(c,l,inn)
            if inn:
                maxx = max(maxx,c+1)
                inn = False    
            else:
                c = 0
                l += 1
        return maxx