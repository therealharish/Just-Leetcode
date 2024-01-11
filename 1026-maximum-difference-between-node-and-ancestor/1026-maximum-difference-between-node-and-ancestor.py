# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def traverse(root,prevmin,prevmax):
            
            if root:

                res[0]=max(abs(prevmin-root.val),abs(prevmax-root.val),res[0])

                prevmin=min(prevmin,root.val)
                prevmax=max(prevmax,root.val)
                traverse(root.left,prevmin,prevmax)
                traverse(root.right,prevmin,prevmax)

        
        
        
        res=[float("-inf")]
        traverse(root,root.val,root.val)
        return res[0]