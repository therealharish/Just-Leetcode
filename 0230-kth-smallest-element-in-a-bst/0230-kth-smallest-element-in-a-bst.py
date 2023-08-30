# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = 0
        def solve(root):
            nonlocal ans
            nonlocal k
            if not root:
                return 
            solve(root.left)
            print(root.val)
            k -= 1
            if k == 0:
                ans = root.val
                return
            solve(root.right)
        
        solve(root)
        return ans