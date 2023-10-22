class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        l = r = k
        m = nums[k]
        ans = nums[k]
        while l > 0 or r < len(nums)-1:
            left = nums[l-1] if l > 0 else float('-inf')
            right = nums[r + 1] if r < len(nums) - 1 else float('-inf')
            if left > right:
                l -= 1
                m = min(m, left)
            else:
                r += 1
                m = min(m, right)
            ans = max(ans, m * (r-l+1))
        return ans
