# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        def solve(root, currentSum):
            
            if not root:
                return False
            
            if not root.left and not root.right:
                if currentSum + root.val == targetSum:
                    return True
                else:
                    return False

            left = solve(root.left, currentSum + root.val)
            right = solve(root.right, currentSum + root.val)
            return left or right

        return solve(root, 0)