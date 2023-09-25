# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(s, t):
            if not s and not t:
                return True
            if s and not t:
                return False
            if not s and t:
                return False
            if s.val == t.val:
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)
            else:
                return False

        def isSub(s, t):
            if not s and t:
                return False
            if s and not t:
                return True
            if sameTree(s, t):
                return True
            return isSub(s.left, t) or isSub(s.right, t)
        
        return isSub(root, subRoot)
        