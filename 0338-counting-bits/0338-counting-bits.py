class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = 0
        arr = []
        for i in range(n+1):
            b = bin(i)
            # print(b)
            cnt = b.count('1')
            # print(cnt)
            arr.append(cnt)
        return arr
        