# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:


        @cache
        def solve(n):

            if n == 0:
                return []
            
            if n == 1:
                return [TreeNode(0)]

            res = []
            for i in range(n):
                l = i
                r = n - i - 1
                leftTrees = solve(l)
                rightTrees = solve(r)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        res.append(TreeNode(0, leftTree, rightTree))
            return res
        
        return solve(n)
        
