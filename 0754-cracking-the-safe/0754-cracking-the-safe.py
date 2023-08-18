class Solution:
    def crackSafe(self, n: int, k: int) -> str:

        total = k**n-1
        start = '0' * n
        visited = set()
        visited.add('0' * n)
        self.ans = '0' * n

        def dfs(total,start):
            if total == 0: 
                return True
            for i in range(k):
                last = start[1:n]
                #print(last+str(i))
                end = last+str(i)
                if end not in visited:
                    visited.add(end)
                    total = total-1
                    self.ans = self.ans+str(i)
                    if dfs(total, end):
                        return True
                    else:
                        visited.remove(end)
                        total = total+1
                        self.ans = self.ans[:-1]
                        #print("l")
            return False

        dfs(total,start)
        return self.ans



