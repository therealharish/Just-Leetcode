class Solution:
    def isPowerOfFour(self, n: int) -> bool:
      count = 0
      for i in range(32):
        if(n&1!=0):
          count+=1
          if(i%2==1):
            return False
        n=n>>1
      
      if(count==1):
        return True
      else:
        return False
          
        