class Solution:
    def minDeletions(self, s: str) -> int:
        count=sorted(collections.Counter(s).values())
        s=set()
        ans=0
        for x in count:
            while x in s and x>0:
                x-=1
                ans+=1

            s.add(x)
        return ans        