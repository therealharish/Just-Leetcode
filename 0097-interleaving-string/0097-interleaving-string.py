class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def solve(a, b, c):
            
            if a < 0 and b < 0 and c < 0:
                return True
            
            if a < 0 and b < 0:
                return False
            
            if c < 0:
                return False
            
            res = False
            if a >=0 and s1[a] == s3[c]:
                res = res or (solve(a-1, b, c-1))
            if b >=0 and s2[b] == s3[c]:
                res = res or (solve(a, b-1, c-1))
                
            return res
            
            
        return solve(len(s1)-1, len(s2)-1, len(s3)-1)