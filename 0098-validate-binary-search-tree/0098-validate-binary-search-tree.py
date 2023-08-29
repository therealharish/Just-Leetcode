# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root, minVal, maxVal):
            
            if not root:
                return True
            if minVal < root.val < maxVal:
                return solve(root.left, minVal, root.val) and solve(root.right, root.val, maxVal)
        
        return solve(root, float('-inf'), float('inf'))