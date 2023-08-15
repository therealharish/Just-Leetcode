# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = ListNode()
        l2 = ListNode()
        l1temp = l1
        l2temp = l2
        temp = head
        while(temp):
            if(temp.val<x):
                l1temp.next = temp
                l1temp = l1temp.next
            else:
                l2temp.next = temp
                l2temp = l2temp.next
            temp = temp.next
        l2temp.next = None
        l1temp.next = l2.next
        return l1.next

