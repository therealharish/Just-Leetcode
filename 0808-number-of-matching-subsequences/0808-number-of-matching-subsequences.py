
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def isSubSequence(word):
            
            start = 0
            for char in word:
                idx = s.find(char, start)
                if idx == -1:
                    return False
                start = idx + 1
            return True
            
        
        count = 0
        
        for word in words:
            
            if isSubSequence(word):
                count += 1
                
        return count
    