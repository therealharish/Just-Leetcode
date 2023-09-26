class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        freq = Counter(s)
        visited = set()
        st = []
        for i in s:
            while st and ord(st[-1]) > ord(i) and freq[st[-1]] > 0 and i not in visited:
                p = st.pop(-1)
                visited.remove(p)
            if i not in visited:
                st.append(i)
                visited.add(i)
            freq[i] -= 1
            # print(st)
        return "".join(st)