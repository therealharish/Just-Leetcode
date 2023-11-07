class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minHeap = []
        for i in range(len(dist)):
            heappush(minHeap, math.ceil(dist[i]/speed[i]))
            
        count = 0
        while(minHeap):
            t = heappop(minHeap)
            if t-count <= 0:
                return count
            
            count += 1
            
        return count