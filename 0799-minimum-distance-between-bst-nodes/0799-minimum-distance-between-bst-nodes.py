# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    mini = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def in_order_trav(root):
            if root.left:
                self.minDiffInBST(root.left)
            if self.prev:
                if abs(root.val - self.prev.val) < self.mini:
                    self.mini = root.val - self.prev.val
            self.prev = root
            if root.right:
                self.minDiffInBST(root.right)

        in_order_trav(root)
        return self.mini