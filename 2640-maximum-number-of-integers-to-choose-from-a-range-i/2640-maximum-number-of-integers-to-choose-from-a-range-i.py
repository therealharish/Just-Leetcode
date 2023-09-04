class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sets = set(banned)
        count, max_sum = 0,0
        for i in range(1, n+1):
            if i not in sets:
                count += i
                if  count > maxSum:
                    break
                else:
                    max_sum += 1
        return max_sum