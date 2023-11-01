# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        currStreak = 1
        currElement = None
        maxElement = 0
        maxStreak = 0
        def solve(root):
            nonlocal currStreak
            nonlocal currElement
            nonlocal maxElement
            nonlocal maxStreak
            if not root:
                return
            solve(root.left)
            if root.val == currElement:
                currStreak += 1
            else:
                currElement = root.val
                currStreak = 1
            # print(maxElement)
            if currStreak == maxStreak:
                maxElement.append(root.val)
            elif currStreak > maxStreak:
                maxElement = [root.val]
                maxStreak = currStreak
            solve(root.right)

        solve(root)
        return maxElement



