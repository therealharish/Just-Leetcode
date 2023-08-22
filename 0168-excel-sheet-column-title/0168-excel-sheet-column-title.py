class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        s = ""
        d = {i:chr(i+64) for i in range(1,27)}
        while columnNumber:
            
            n = (columnNumber-1) % 26
            s = d[n+1] + s
            columnNumber = (columnNumber-1) // 26   
        return s