# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxi = -float('inf')
        def solve(root):
            nonlocal maxi
            if not root:
                return 0
            leftSum = max(0,solve(root.left) )
            rightSum = max(0, solve(root.right))
            maxi = max(maxi, leftSum + rightSum + root.val)
            return root.val + max(leftSum, rightSum)
        solve(root)
        return maxi