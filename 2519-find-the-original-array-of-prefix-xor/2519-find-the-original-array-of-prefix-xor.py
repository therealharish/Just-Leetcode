class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        ans = [pref[0]]
        xor = pref[0]
        for i in range(1, len(pref)):
            xor = pref[i-1] ^ pref[i]
            ans.append(xor)
        return ans

        