# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) != len(postorder):
            return None
    
        d = {}
        for i, ele in enumerate(inorder):
            d[ele] = i
            
        def solve(inorderStart, inorderEnd, postorderStart, postorderEnd):
            
            if postorderEnd < postorderStart or inorderEnd < inorderStart:
                return None
            
            rootVal = postorder[postorderEnd]
            root = TreeNode(rootVal)
            inorderIndex = d[rootVal]
            itemsInLeft = inorderIndex - inorderStart
            
            root.left = solve(inorderStart, inorderIndex - 1, postorderStart, postorderStart + itemsInLeft - 1)
            root.right = solve(inorderIndex + 1, inorderEnd, postorderStart + itemsInLeft, postorderEnd - 1)
            
            return root
        
        return solve(0, len(inorder) - 1, 0, len(postorder) - 1)
            
                
        