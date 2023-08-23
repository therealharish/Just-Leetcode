class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)
        maxHeap = []
        ans = ""
        for char, count in freq.items():
            maxHeap.append((-count, char))
        
        heapify(maxHeap)
        prev = None
        print(maxHeap)
        while(maxHeap or prev):
            if not maxHeap and prev:
                return ""
            cnt, char = heappop(maxHeap)
            ans += char
            cnt += 1
            if prev:
                heappush(maxHeap, prev)
            prev = None
            if cnt < 0:
                prev = (cnt, char)
        return ans


