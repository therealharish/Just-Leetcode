class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        hp= []
        for i, n in enumerate(nums):
            heappush(hp, (n, i))
            if len(hp) > k:
                heappop(hp)
        hp.sort(key = lambda x: x[1])
        return [i[0] for i in hp]