class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = collections.Counter(t)
        for i in s:
            if i in dic:
                dic[i] -= 1
        for k,v in dic.items():
            if dic[k] == 1:
                return k