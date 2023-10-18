# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if not root:
            return []
        q = deque()
        q.append(root)
        i = 0
        while(q):
            level = []
            for j in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if i % 2 == 0:
                ans.append(level.copy())
            else:
                ans.append(level[::-1])
            i+=1
        return ans