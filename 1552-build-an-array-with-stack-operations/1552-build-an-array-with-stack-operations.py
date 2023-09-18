class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        z=[]
        for i in range(1,n+1):
            if len(z)==len(target):
                break
            else:

                if i not in target :
                    s.append("Push")
                    s.append("Pop")
                else:
                    s.append("Push")
                    z.append(i)

        return s