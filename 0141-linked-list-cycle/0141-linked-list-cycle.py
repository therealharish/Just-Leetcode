# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while(head):
            if(head in visited):
                return True
            visited.add(head)
            head = head.next
        return False
    

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False    
        fast = head.next
        slow = head
        while(fast and slow!=fast):
            slow = slow.next
            fast = fast.next
            if(not fast):
                break
            fast = fast.next
        return fast!=None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        slow = head
        fast = head.next
        while fast and slow!=fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
        return fast!=None
                
        