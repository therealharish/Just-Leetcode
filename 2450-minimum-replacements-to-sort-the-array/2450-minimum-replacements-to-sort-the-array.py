class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        m = nums[-1]
        count = 0
        for i in range(len(nums)-2, -1, -1):
            curr = nums[i]
            if curr > m:
                print(curr, m)
                parts = ceil(curr / m)
                # print(parts)
                count += parts - 1
                m = curr // parts
            else:
                m = curr
        return count    
