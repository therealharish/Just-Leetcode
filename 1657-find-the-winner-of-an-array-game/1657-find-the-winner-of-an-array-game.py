class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k>=n:
            return max(arr)
        
        i,j = 0,1
        ans = 0
        while j<n and ans<k:
            if arr[i] > arr[j]:
                j += 1
                ans += 1
            else:
                i = j
                j += 1
                ans = 1

        return arr[i]