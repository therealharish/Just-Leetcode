# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def find(root, path):
            nonlocal longestPath
            if not root:
                return 
            
            path.append(root)
            
            if(not root.left and not root.right):
                longestPath = max(longestPath, len(path))
            
            find(root.left, path.copy())
            find(root.right, path.copy())
    
        longestPath = 0            
        find(root, [])
        return longestPath
                    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        @cache
        def solve(root):

            if not root:
                return 0
            
            return 1 + max(solve(root.left), solve(root.right))

        return solve(root)