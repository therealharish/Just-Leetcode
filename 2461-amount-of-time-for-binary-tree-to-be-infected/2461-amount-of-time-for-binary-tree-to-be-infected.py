# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def addParentAndFindStart(node, parent):
            if node:
                node.parent = parent

                if node.val == start: 
                    nonlocal startNode
                    startNode = node

                addParentAndFindStart(node.left, node)
                addParentAndFindStart(node.right, node)
        
        startNode = None
        addParentAndFindStart(root, None)

        visited = set()

        def maxDepth(node):
            if node in visited: return 0
            else:
                visited.add(node)

                parent_depth = maxDepth(node.parent) if node.parent else 0
                left_depth = maxDepth(node.left) if node.left else 0
                right_depth = maxDepth(node.right) if node.right else 0
                
                return 1 + max(parent_depth, left_depth, right_depth)

        return maxDepth(startNode) - 1