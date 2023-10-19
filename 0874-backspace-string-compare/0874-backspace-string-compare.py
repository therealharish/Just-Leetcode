class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

      def nextValidIndex(str, point):
        backspace = 0
        while(True):
          if(point<0):
            return -1
          if(str[point] == "#"):
            backspace+=1
            point-=1
          elif(backspace):
            point-=1
            backspace-=1
          else:
            return point
          
          
      
      i = len(s)-1
      j = len(t)-1
      while(True):
        i = nextValidIndex(s, i)
        j = nextValidIndex(t, j)
        if(i<0 and j<0):
          return True
        elif(i<0 or j<0):
          return False
        elif(s[i] != t[j]):
          return False
        else:
          i-=1
          j-=1
        
      
          