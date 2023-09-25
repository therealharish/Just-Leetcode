class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        def startWith(a,b):
            ptr1,ptr2 = 0,0
            while ptr1 < len(a) and ptr2 < len(b) and a[ptr1] == b[ptr2]:
                ptr1 += 1
                ptr2 += 1
            return ptr1 == len(a)
        def endWith(a,b):
            ptr1,ptr2 = len(a) - 1,len(b) - 1
            while ptr1 >= 0 and ptr2 >= 0 and a[ptr1] == b[ptr2]:
                ptr1 -= 1
                ptr2 -= 1
            return ptr1 == -1
        hmap = defaultdict(int)
        size = len(nums)
        ans = 0
        for i in range(size):
            op1 = startWith(nums[i],target)
            if op1 == True:
                remain1 = target[len(nums[i]):]
                if remain1 in hmap:
                    ans += hmap[remain1]
            op2 = endWith(nums[i],target)
            if op2 == True:
                remain2 = target[:len(target)-len(nums[i])]
                if remain2 in hmap:
                    ans += hmap[remain2]
            hmap[nums[i]] += 1
        return ans