# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        key = 0
        def solve(root):
            nonlocal key
            if not root:
                return
            solve(root.right)
            root.val = root.val + key
            key = root.val
            solve(root.left)
        solve(root)
        return root


        