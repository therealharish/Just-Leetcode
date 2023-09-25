# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def solve(root):
            if not root:
                return (True, 0)
            left = solve(root.left)
            right = solve(root.right)
            print(left, right)
            if not left[0] or not right[0]:
                return (False, 10**9)
            if abs(left[1]-right[1])<=1:
                return (True, 1 + max(left[1], right[1]))
            else:
                return (False, 1+max(left[1], right[1]))
        
        return solve(root)[0]
        