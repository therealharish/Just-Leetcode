# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        height = 0
        ans = root.val
        def solve(i, root):
            nonlocal height
            nonlocal ans
            
            if not root:
                return
            
            if i > height:
                height = i
                ans = root.val
            solve(i+1, root.left)
            solve(i+1, root.right)

        solve(0, root)
        return ans
        