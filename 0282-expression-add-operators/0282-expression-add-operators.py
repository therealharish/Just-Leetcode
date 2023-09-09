class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        res = []
        def solve(i, curResult, curSum, prev):

            if i >= len(num):
                if curSum == target:
                    res.append(curResult)
                    return

            for j in range(i, len(num)):
                curStr = num[i: j+1]
                if not curResult:
                    solve(j+1, curStr, int(curStr), curStr)
                else:
                    solve(j+1, curResult + "+" + curStr, curSum + int(curStr), curStr)
                    solve(j+1,  curResult + "-" + curStr, curSum - int(curStr), "-"+curStr)
                    solve(j+1,  curResult + "*" + curStr, curSum - int(prev) + int(curStr) * int(prev), str(int(curStr)*int(prev)))

                if curStr == "0":
                    break
        
        solve(0, "", 0, 0)
        return res