# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append([root, 0])
        ans = 0
        while q:
            size = len(q)
            arr = []
            for i in range(size):
                node, idx = q.popleft()
                arr.append(idx)
                if node.left:
                    q.append([node.left, idx*2])
                if node.right:
                    q.append([node.right, idx*2+1])
            ans = max(ans, arr[-1]-arr[0]+1)
        return ans
                
        