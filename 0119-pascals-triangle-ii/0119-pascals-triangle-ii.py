class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            temp = [1]
            if not ans:
                ans.append(temp)
            else:
                for j in range(1, len(ans[-1])):
                    temp.append(ans[-1][j]+ans[-1][j-1])
                temp.append(1)
                ans.append(temp)
                print(ans)
        return ans[-1]
