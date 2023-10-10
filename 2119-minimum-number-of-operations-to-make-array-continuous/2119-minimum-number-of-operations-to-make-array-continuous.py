class Solution:
    def minOperations(self, nums: List[int]) -> int:
                
        n = len(nums)
        ans = n
        nums.sort()
        cnt = Counter(nums)
        
        # build key for repeated occurance
        repeat = sorted(k for k in cnt if cnt[k] > 1)
        
        # build prefix sum for repeated occurance need to be changed
        repeat_change = list(accumulate([cnt[x] - 1 for x in repeat], initial=0))


        for i in range(n):
            # numbers left side all need to be changed
            left = i
            
            # numbers right side all need to be changed
            loc = bisect.bisect(nums, nums[i] + n - 1)
            right = n - loc
            
            # calculate occurance of repeated number within [nums[i], nums[i] + n - 1]
            repeat_l = bisect.bisect_left(repeat, nums[i])
            repeat_r = bisect.bisect(repeat, nums[i] + n - 1)
            ans = min(ans, left + right + repeat_change[repeat_r] - repeat_change[repeat_l])
        
        return ans