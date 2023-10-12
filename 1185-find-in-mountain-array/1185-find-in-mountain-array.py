# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        
        low, high = 0, n-1
            
        while low < high:
            mid = (low + high)//2

            if mountain_arr.get(mid) < mountain_arr.get(mid+1) and mid + 1 < n:
                low = peak = mid + 1
            else:
                high = mid

        low, high = 0, peak
        
        while low <= high:
            mid = (low + high)//2

            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1

        low, high = peak, n-1

        while low <= high:
            mid = (low + high)//2

            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
        