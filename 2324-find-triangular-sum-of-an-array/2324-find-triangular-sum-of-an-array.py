import numpy as np
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        newArr = nums
        for i in range(1,n):
            tmp = np.empty([n-i],int)
            for j in range(n-i):
                tmp[j] = (newArr[j]+newArr[j+1])%10
            newArr = tmp
        return newArr[0]