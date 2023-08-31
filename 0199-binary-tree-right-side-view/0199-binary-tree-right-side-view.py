# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        def solve(root, level):
            if not root:
                return None
            if level == len(ans):
                ans.append(root.val)
            solve(root.right, level + 1)
            solve(root.left, level + 1)
        solve(root, 0)
        return ans
