class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = []
        
        for i in range(k):
            heappush(mh, nums[i])
        
        for i in range(k, len(nums)):
            if(nums[i]>mh[0]):
                heappop(mh)
                heappush(mh, nums[i])

        return mh[0]