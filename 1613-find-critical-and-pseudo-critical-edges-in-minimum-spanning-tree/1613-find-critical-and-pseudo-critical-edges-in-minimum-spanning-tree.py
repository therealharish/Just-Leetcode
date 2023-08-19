class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        originalEdges = edges[:]
        edges = sorted(edges, key = lambda x: x[2])

        def kruskalUsingDSU(edges, includeEdge = None, excludeEdge = None):
            print(includeEdge, excludeEdge)
            parent = [i for i in range(n)]
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                p1 = find(x)
                p2 = find(y)
                if p1!=p2:
                    parent[p2] = p1
                    return True
                else:
                    False
            
            mst = []
            cost = 0
            if includeEdge:
                if union(includeEdge[0], includeEdge[1]):
                    cost += includeEdge[2]
            for u, v, w in edges:
                if [u, v, w] == includeEdge or [u, v, w] == excludeEdge:
                    continue
                if union(u, v):
                    cost += w
            return cost
        
        originalCost = kruskalUsingDSU(edges)
        print(originalCost)
        critical = []
        pseudoCritical = []
        for i in range(len(originalEdges)):
            exclude = kruskalUsingDSU(edges, None,  originalEdges[i])
            include = kruskalUsingDSU(edges, originalEdges[i], None)
            if exclude > originalCost or exclude < originalCost:
                critical.append(i)
            elif include == originalCost:
                pseudoCritical.append(i)
                
        return [critical, pseudoCritical]
            
                
        
        
        
        