"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):        
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def check(x1, y1, x2, y2):
            # print("check", x1, y1, x2, y2)
            num = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    # print(i, j)
                    if grid[i][j] != num:
                        return 2
            return num                   
            
        def solve(x1, y1, x2, y2):
            num = check(x1, y1, x2, y2)
            # print(x1, y1, x2, y2, num)
            if num == 2:
                topLeft = solve(x1, y1, (x1+x2)//2, (y1+y2)//2)
                topRight = solve(x1, (y1+y2)//2, (x1+x2)//2, y2)
                bottomLeft = solve((x1+x2)//2, y1, x2, (y1+y2)//2)
                bottomRight = solve((x1+x2)//2, (y1+y2)//2, x2, y2)
                return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
            else:
                return Node(num, 1, None, None, None, None)
        
        return solve(0, 0, n, n)
            
            