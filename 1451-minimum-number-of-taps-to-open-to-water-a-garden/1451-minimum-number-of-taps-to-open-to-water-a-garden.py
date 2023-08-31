class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = [0] * len(ranges) 
        for i,r in enumerate(ranges):
            left = max(0, i - r)
            taps[left] = max(taps[left], i + r)

        total = reach = nextReach = 0
        for i, r in enumerate(taps):
            nextReach = max(nextReach, r)
            
            if i == reach:
                if nextReach == reach: return -1
                
                total += 1
                reach = nextReach
                if (nextReach >= n): break
        
        return total