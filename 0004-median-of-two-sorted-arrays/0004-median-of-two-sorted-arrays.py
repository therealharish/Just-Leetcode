class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        left = (n1 + n2 + 1) // 2
        if n1 < n2:
          A = nums1
          B = nums2
        else:
          A = nums2
          B = nums1
          n1, n2 = n2, n1
        
        low = 0
        high = n1
        while(low <= high):
          mid = (low + high) // 2
          cut1 = mid
          cut2 = left - mid
          l1 = -float('inf') if cut1 == 0 else A[cut1-1]
          l2 = -float('inf') if cut2 == 0 else B[cut2-1]
          r1 = float('inf') if cut1 == n1 else A[cut1]
          r2 = float('inf') if cut2 == n2 else B[cut2]
          if l1 <= r2 and l2 <= r1:
            if (n1+n2)%2 == 1:
              return max(l1, l2)
            else:
              return (max(l1, l2)+min(r1, r2))/2
          elif l1 > r2:
            high = cut1 - 1
          else:
            low = cut1 + 1
        

