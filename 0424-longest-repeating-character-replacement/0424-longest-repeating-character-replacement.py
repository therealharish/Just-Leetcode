class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ws = 0
        res = 0
        d = {}
        for we in range(len(s)):
            curr = s[we]
            d[curr] = d.get(curr, 0) + 1
            check = (we-ws+1) - max(d.values()) 

            if check <= k:
                res = max(res, we-ws+1)
            else:
                d[s[ws]] -= 1
                ws += 1
        return res

        