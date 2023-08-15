class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arrB = []
        arr = [pivot] * nums.count(pivot)
        for x in nums:
            if x< pivot:
                arrB.append(x)
            elif x> pivot:
                arr.append(x)
        return arrB +arr