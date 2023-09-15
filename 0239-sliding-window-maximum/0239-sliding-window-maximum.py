class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque([])
        ans = []
        for i in range(k):
            if(d and nums[i]<=nums[d[0]]):
                d.appendleft(i)
            elif(d and nums[i]>=nums[d[0]]):
                while(d and nums[i]>=nums[d[0]]):
                    d.popleft()
                d.appendleft(i)
            else:
                d.appendleft(i)
        ans.append(nums[d[-1]])
        for i in range(k, len(nums)):
            if(d and nums[i]<=nums[d[0]]):
                d.appendleft(i)
                if(d[-1]<=(i-k)):
                    d.pop()
            elif(d and nums[i]>=nums[d[0]]):
                while(d and nums[i]>nums[d[0]]):
                    d.popleft()
                if(d and d[-1]<=(i-k)):
                    d.pop()
                d.appendleft(i)
                
            else:
                d.appendleft(i)
            ans.append(nums[d[-1]])
        return ans
        
            
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def nextGreaterElement(arr):
            st = []
            ans = [len(arr)]*len(arr)
            for i in range(len(arr)-1, -1, -1):
                curr = arr[i]
                while(st and curr>=arr[st[-1]]):
                    st.pop()
                if(st):
                    ans[i] = st[-1]
                st.append(i)
            return ans
        
        nextGreater = nextGreaterElement(nums)
        # print(nextGreater)
        ans = []
        j = 0
        for i in range(len(nums)-k+1):
            if(j<i):
                j = i
            while(nextGreater[j]<i+k):
                j = nextGreater[j]
            ans.append(nums[j])
        return ans

# O(n) + O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []
        for i in range(len(nums)):
            if (dq and dq[0]<=(i-k)):
                # print("smaller", dq)
                dq.popleft()
            while(dq and nums[dq[-1]]<nums[i]):
                # print("ele", dq)
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans

# O(n) + O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []
        for i in range(len(nums)):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while(dq and nums[dq[-1]]<nums[i]):
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans

