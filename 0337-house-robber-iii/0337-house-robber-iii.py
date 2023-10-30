# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def f1(root): 
            ''' defines that we are either picking or not picking'''
            if not root:
                return 0
            choose = root.val
            unchoose = 0
            return max(choose + f2(root.left) + f2(root.right), unchoose + f1(root.left) + f1(root.right))
        
        @cache
        def f2(root):
            ''' defines that it's parent has been picked'''
            if not root:
                return 0
            return f1(root.left) + f1(root.right)

        return f1(root)
            