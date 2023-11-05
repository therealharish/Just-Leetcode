class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        if not right:
            return max(left)
        if not left:
            return n - min(right)
        
        l = max(left)
        r = n - min(right)
        
        return max(l,r)
                        
                        