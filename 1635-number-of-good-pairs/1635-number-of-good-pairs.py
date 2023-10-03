class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = Counter(nums)
        ans = 0
        for key, val in count.items():
            ans += val*(val-1)//2
        return ans
        