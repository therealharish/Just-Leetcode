class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        temp = ""
        for i in range(0, len(s)-1):
            temp += s[i]
            l = len(s)//len(temp)
            # print(temp*l)
            if temp*l == s:
                return True
        return False
                
                