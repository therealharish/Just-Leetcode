# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def solve(root):
            if not root:
                return None
            if root.val == key:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                temp = root.left
                while(temp.right):
                    temp = temp.right
                temp.right = root.right
                return root.left
            else:
                if root.val > key:
                    root.left = solve(root.left)
                else:
                    root.right = solve(root.right)
                return root

        dummy = solve(root)
        return dummy


        