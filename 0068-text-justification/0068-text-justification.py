class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        ans = []
        line = []
        length = 0
        while ( i < len(words)):
            curr = words[i]
            if length + len(line) - 1 + len(curr) >= maxWidth:
                difference = maxWidth - length
                spaces = difference // max(1, len(line) - 1)
                remaining = difference % max(1, len(line) - 1)
                
                for j in range(max(1, len(line)-1)):
                    line[j] += " " * spaces
                    if remaining: 
                        line[j] += " "
                        remaining -= 1
                
                ans.append("".join(line))
                line = []
                length = 0
            else:
                line.append(curr)
                length += len(curr)
                i += 1
                
        last = " ".join(line)
        last += " " * (maxWidth - len(last))
        ans.append(last)
            
        return ans    
            
            