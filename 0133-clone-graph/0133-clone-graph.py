"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        adj = defaultdict(list)

        if not node:
            return None

        visited = set()
        def dfs(node):
            if not node or node in visited:
                return
            visited.add(node)
            adj[node.val] = []
            for nbr in node.neighbors:
                adj[node.val].append(nbr.val)
                dfs(nbr)

        dfs(node)
        
        # print(adj)
        
        hm = {}

        for key, val in adj.items():
            hm[key] = Node(key)

        print(hm)

        for key, val in adj.items():
            print(key, val, hm[key].val, hm[key].neighbors)
            for nbr in val:
                print(hm[nbr], hm[nbr].val)
                hm[key].neighbors.append(hm[nbr])

        for key, val in hm.items():
            return val


    

        



