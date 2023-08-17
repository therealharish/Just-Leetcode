# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found = False
        
        def check(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return check(root.left, subRoot.left) and check(root.right, subRoot.right)

        def solve(root, subRoot):
            if not root:
                return
            if root.val == subRoot.val:
                ans = check(root, subRoot)
                if ans:
                    return True

            return solve(root.left, subRoot) or solve(root.right, subRoot)

        return solve(root, subRoot)
            
        