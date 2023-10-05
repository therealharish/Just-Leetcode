class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ele1 = -1
        ele2 = -1
        count1 = 0
        count2 = 0
        for i in nums:
            if ele1 == i:
                count1 += 1
            elif ele2 == i:
                ele2 = i
                count2 += 1
            else:
                if ele1 != i and count1 == 0:
                    ele1 = i
                    count1 += 1
                elif ele2 != i and count2 == 0:
                    ele2 = i
                    count2 += 1
                else:
                    count1 -=1 
                    count2 -= 1
        
        ans = []
        if nums.count(ele1) > len(nums)//3:
            ans.append(ele1)
        if ele1!=ele2 and nums.count(ele2) > len(nums)//3:
            ans.append(ele2)
    
        return ans
