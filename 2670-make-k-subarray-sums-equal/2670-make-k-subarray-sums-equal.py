class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        k = gcd(k, len(arr))

        lookup = defaultdict(list)

        for i in range(len(arr)):
            lookup[i % k].append(arr[i])


        ans = 0

        for key in lookup:
            vals = lookup[key]
        
            vals.sort()

            median = len(vals) // 2
            medianVal = vals[median] if len(vals) % 2 else (vals[median] + vals[median - 1]) // 2


            for val in vals:
                ans += abs(val - medianVal)

        return ans