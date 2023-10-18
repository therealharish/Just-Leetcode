# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        ans = float('inf')
        prev = None
        def solve(root):
            nonlocal ans
            nonlocal prev
            if root.left:
                solve(root.left)
            if prev:
                ans = min(ans, abs(root.val - prev.val))
            prev = root
            if root.right:
                solve(root.right)
        
        solve(root)
        return ans

        