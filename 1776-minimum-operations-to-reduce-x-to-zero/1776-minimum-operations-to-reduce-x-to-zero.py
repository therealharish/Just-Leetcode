class Solution1:
    def minOperations(self, nums: List[int], x: int) -> int:
        S = sum(nums)
        left = right = curr = 0
        ans = -1
        while right<len(nums):
            curr += nums[right]
            right+=1
            while left<len(nums) and curr>S-x:
                curr-=nums[left]
                left+=1
            if curr == S-x:
                ans = max(ans,right-left)
                
        return len(nums) - ans if ans!=-1 else ans

# O(n^3) - MLE/TLE
class Solution2:
    def minOperations(self, nums: List[int], x: int) -> int:

        if sum(nums) < x:
            return -1

        @cache
        def solve(i, j, x):
            if i >= len(nums) or j < 0 or i > j or x == 0:
                return 0
            if x < 0:
                return 10**9
            # print(i, j)
            left = 1 + solve(i+1, j, x-nums[i])
            right = 1 + solve(i, j-1, x-nums[j])
            return min(left, right)

        ans =  solve(0, len(nums)-1, x)
        if ans >= 10**9:
            return -1
        else:
            return ans

# rahul sir's approach - works because all are pos
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        left = 0
        s = 0
        ans = -1
        
        while(left < len(nums)):
            if s + nums[left] <= x:
                s += nums[left]
                left += 1
            else:
                break
        print(s)
        if s == x:
            ans = left
        right = len(nums)-1
        left -= 1
        
        while(right>=0 and left < right):
            print(s)
            while s + nums[right] <= x:
                s += nums[right]
                right -= 1
                if s == x:
                    print('here')
                    if ans == -1:
                        ans = left + len(nums) - right
                    ans = min(ans, left + (len(nums)-right))
            if left >= 0:
                s -= nums[left]
                left -= 1
            else:
                break

            
        return ans

            
