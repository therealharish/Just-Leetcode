# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        div = length // k
        rem = length % k

        ans = []
        while (len(ans)<k):
            # print(ans, div, rem)
            temp = head
            prev = None
            ans.append(temp)
            if rem>0:
                loop = div + 1
            else:
                loop = div
            while (loop):
                if temp:
                    prev = temp
                    temp = temp.next
                loop -= 1
            head = temp
            if prev:
                prev.next = None
            rem -= 1
        return ans
                    

                    