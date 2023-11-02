# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        count = 0
        def solve(root, nodes):
            nonlocal count
            if not root:
                return (0, 0)
            left = solve(root.left, nodes + 1)
            right = solve(root.right, nodes + 1)
            # print(root.val, left, right)
            val = left[0] + right[0] + root.val
            totalNodes = left[1] + right[1] + 1
            if val // totalNodes == root.val:
                count += 1
            return (val, totalNodes)
        solve(root, 0)
        return count
            
        