class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        abc='abcdefghijklmnopqrstuvwxyz'
        n=len(board)
        m=len(board[0])
        def check(a,b):
            la=len(a)
            lb=len(b)
            b_=b[::-1]
            start=[]
            n=0
            for i in range(la):
                if i==0 and (a[i]==" " or a[i] in abc):
                    start.append(i)
                    n+=1
                elif i>0 and (a[i]==" " or a[i] in abc) and a[i-1]=="#":
                    start.append(i)
                    n+=1
                elif i>0 and a[i]=='#' and (a[i-1]==' ' or a[i-1] in abc):
                    start.append(i)
                if i==la-1 and (a[i]==' ' or a[i] in abc):
                    start.append(i+1)
            for i in range(n):
                flag=0
                flag1=0
                if start[2*i+1]-start[2*i] == lb:
                    
                    for j in range(start[2*i],start[2*i+1]):
                        k=j-start[2*i]
                        if not (a[j]==' ' or a[j]==b[k]):
                            # print(a[j],b[k])
                            flag=1
                            break
                    for j in range(start[2*i],start[2*i+1]):
                        k=j-start[2*i]
                        if not (a[j]==' ' or a[j]==b_[k]):
                            # print(a[j],b[k])
                            flag1=1
                            break                   
                    if flag==0 or flag1==0:
                        return True
            return False                          
        new=[["" for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[j][i]=board[i][j]
        s=set()
        for i in range(n):
            s.add("".join(board[i]))
        for i in range(m):
            s.add("".join(new[i]))
        for i in s:
            if check(i,word):
                return True
        return False