class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        root = 0
        l = set(leftChild)
        r = set(rightChild)
        for i in range(n):
            if i not in leftChild and i not in rightChild:
                root = i
                break
    
        visited = set()
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            print(curr)
            if curr in visited:
                return False
            visited.add(curr)
            if leftChild[curr] != -1:
                q.append(leftChild[curr])
            if rightChild[curr] != -1:
                q.append(rightChild[curr])

        if len(visited) == n:
            return True
        else:
            return False

        