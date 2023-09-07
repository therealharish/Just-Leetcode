# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        mylist = []
        
        while curr:
            mylist.append(curr.val)
            curr = curr.next
        
        mylist.sort()
        
        result = ListNode()
        node = result
        
        for val in mylist:
            node.next = ListNode(val)
            node = node.next
        
        return result.next