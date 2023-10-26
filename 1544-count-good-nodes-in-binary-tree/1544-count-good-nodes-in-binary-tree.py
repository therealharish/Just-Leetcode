# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        visited = set()
        def dfs(node, maxParent):
            if not node:
                return 0
            goods = 0
            if node.val >= maxParent:
                goods = 1
            return goods + dfs(node.left, max(maxParent, node.val)) + dfs(node.right, max(maxParent, node.val))
        
        return dfs(root, -float('inf'))


        