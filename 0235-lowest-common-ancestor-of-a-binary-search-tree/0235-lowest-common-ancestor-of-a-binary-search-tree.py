# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        def solve(root):
            if not root:
                return None
            if p.val <= root.val and q.val > root.val:
                return root
            elif p.val < root.val and q.val >= root.val:
                return root
            elif p.val < root.val and q.val > root.val:
                return root
            else:
                if p.val > root.val and q.val > root.val:
                    return solve(root.right)
                else:
                    return solve(root.left)
            
        return solve(root)