class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        minHeap = self.minHeap
        maxHeap = self.maxHeap
        heappush(maxHeap, -num)
        if minHeap and maxHeap and -maxHeap[0] > minHeap[0]:
            val = -heappop(maxHeap)
            heappush(minHeap, val)

        if len(maxHeap) > len(minHeap) + 1:
            val = -heappop(maxHeap)
            heappush(minHeap, val)
        elif len(minHeap) > len(maxHeap) + 1:
            val = heappop(minHeap)
            heappush(maxHeap, -val)
        # print(maxHeap, minHeap)
         
    def findMedian(self) -> float:
        minHeap = self.minHeap
        maxHeap = self.maxHeap
        if len(maxHeap) > len(minHeap):
            return -maxHeap[0]
        if len(minHeap) > len(maxHeap):
            return minHeap[0]
        
        return (minHeap[0]-maxHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()