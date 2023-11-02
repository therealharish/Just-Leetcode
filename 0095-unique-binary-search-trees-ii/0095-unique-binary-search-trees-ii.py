# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def solve(left, right):

            if left > right:
                return [None]
            
            if left == right:
                return [TreeNode(left)]
            
            res = []
            for i in range(left, right + 1):
                leftTrees = solve(left, i-1)
                rightTrees = solve(i+1, right)
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(i, t1, t2))

            return res

        return solve(1, n)
            


def fn(left, right):
    if left > right:
        return [None]
    
    if left == right:
        return [left]
    
    res = []
    for i in range(left, right + 1):
        leftTrees = fn(left, i-1)
        rightTrees = fn(i+1, right)
        for t1 in leftTrees:
            for t2 in rightTrees:
                res.append(i, t1, t2)

    return res
  