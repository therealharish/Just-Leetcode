class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        st = []
        fill = set()
        
        for i in range(1, n+1):

            if len(fill) == len(target):
                break

            if i in target:
                st.append("Push")
                fill.add(i)
            else:
                st.append("Push")
                st.append("Pop")

        return st