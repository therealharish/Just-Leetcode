# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        leftStore = dummy
        curr = head
        for i in range(left - 1):
            leftStore = curr
            curr = curr.next
        
        prev = None
        for i in range(right - left + 1):
            copy = curr.next
            curr.next = prev
            prev = curr
            curr = copy
        
        leftStore.next = prev

        temp = dummy
        while(temp.next):
            temp = temp.next
        temp.next = copy

        return dummy.next