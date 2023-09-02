def dfs(suffix_tree, s, index, visited, score):
    if score <= visited[index]:
        return
    visited[index] = score
    root = suffix_tree
    for next_index in range(index + 1, len(s) + 1):
        letter = s[next_index - 1]
        if letter in root[0]:
            root = root[0][letter]
        else:
            root = [{}, False]
        if root[1]:
            dfs(suffix_tree, s, next_index, visited, score + next_index - index)
        else:
            dfs(suffix_tree, s, next_index, visited, score)

class Solution:
    def minExtraChar(self, s: str, words: List[str]) -> int:
        visited = defaultdict(lambda: -1)
        suffix_tree = [{}, False]
        # N^2. The suffix_tree is simply built to prevent string slicing in the DFS or during graph building
        for word in words:
            root = suffix_tree
            for letter in word:
                if letter not in root[0]:
                    root[0][letter] = [{}, False]  
                root = root[0][letter]
            root[1] = True
        # DFS is N^3 overall: number_of_dfs_visits * cost_per_dfs
        # number_of_dfs_visits: Each node in DFS can be visited N times at most (N times you find a better score)
        # cost_per_dfs: N
        dfs(suffix_tree, s, 0, visited, 0)
        return max(0, len(s) - max(visited.values()))