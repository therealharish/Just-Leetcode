class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def fn(i, j): 
            """Return max dot product of nums1[i:] and nums2[j:]."""
            if i == len(nums1) or j == len(nums2): return -inf
            return max(nums1[i]*nums2[j] + fn(i+1, j+1), nums1[i]*nums2[j], fn(i+1, j), fn(i, j+1))
        
        return fn(0, 0)