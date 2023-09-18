class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        maxHeap = []
        for i, arr in enumerate(mat):
            c = arr.count(1)
            
            if i < k:
                heappush(maxHeap, (-c, -i))
            else:
                if (-maxHeap[0][0]) > c:
                    heappop(maxHeap)
                    heappush(maxHeap, (-c, -i))
            print(maxHeap, -maxHeap[0][0])
        ans = []
        print(maxHeap)
        for i in range(k):
            p = heappop(maxHeap)
            ans.append(-p[1])
        return ans[::-1]

