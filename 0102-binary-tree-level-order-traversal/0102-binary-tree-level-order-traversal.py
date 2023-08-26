# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        ans = []
        queue = [root]
        while(queue):
            l = len(queue)
            a = []
            for i in range(l):
                node = queue.pop(0)
                a.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            ans.append(a)
        return ans
                
                
                
        