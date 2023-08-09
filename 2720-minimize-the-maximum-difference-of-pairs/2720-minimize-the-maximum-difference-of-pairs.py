class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(target):
            i, cnt = 0,0
            while i < len(nums)-1:
                if abs(nums[i+1]-nums[i])<=target:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
        
        if p==0 or len(nums)==0:
            return 0
        
        nums.sort()
        arr = set()
        for i in range(len(nums)-1):
            arr.add(nums[i+1]-nums[i])
        arr = sorted(arr)
        l , r = 0, len(arr)
        
        while l<=r:
            m = (l+r)//2
            if isValid(arr[m]):
                r=m-1
                res = arr[m]
            else:
                l=m+1
        return res