import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False
        st = int(math.sqrt(n))
        for i in range(2,st+1):
            if is_prime:
                for j in range(i*i,n,i):
                    is_prime[j] = False
        return sum(is_prime)