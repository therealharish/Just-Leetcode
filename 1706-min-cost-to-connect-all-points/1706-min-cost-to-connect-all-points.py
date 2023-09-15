class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        parent = [i for i in range(len(points))]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                return True
            else:
                return False

        def find(a):
            if a!=parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        l = []
        ans = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                fromx, fromy = points[i]
                tox, toy = points[j]
                dist = abs(fromx-tox)+abs(fromy-toy)
                l.append((dist, i, j))
        l.sort()
        # print(l)

        for i in range(len(l)):
            dist, fromPoint, toPoint = l[i]
            # print(dist, fromPoint, toPoint)
            if union(fromPoint, toPoint):
                # print('component ', fromPoint, toPoint)
                # print(parent)
                ans += dist
        
        return ans 
        
                
