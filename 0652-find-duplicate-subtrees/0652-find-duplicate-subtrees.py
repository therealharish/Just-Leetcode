# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hm = {}
        ans = []
        def solve(root):
            nonlocal ans
            if not root:
                return "#"
            s = str(root.val) + "," + solve(root.left) + "," + solve(root.right)
            if s in hm:
                ans.append(hm[s])
            else:
                hm[s] = root
            return s
        
        solve(root)
        return list(set(ans))