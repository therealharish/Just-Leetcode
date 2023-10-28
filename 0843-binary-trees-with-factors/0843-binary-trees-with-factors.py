class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        MOD = 10**9 + 7
        arr.sort()
        ans = len(arr)
        hm = {}
        for i in arr:
            hm[i] = 1
        for i in range(1, len(arr)):
            count = 0
            curr = arr[i]
            for j in range(i):
                if curr % arr[j] == 0 and curr // arr[j] in hm:
                    count += hm[arr[j]] * hm[curr//arr[j]]
            ans += count
            hm[curr] += count

        return ans % MOD
        