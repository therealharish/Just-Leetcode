# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next is None:
            return [-1,-1]
        current = head
        previous = None
        array = []
        last_count = 0
        min_dist = 0
        dist_array = []
        count = 1
        while current.next:
            next = current.next
            if previous is not None:
                if current.val>previous.val and current.val>next.val:
                    array.append(count)
                    if last_count>0:
                        if min_dist == 0:
                            min_dist = count-last_count
                        elif count-last_count<min_dist:
                            min_dist = count-last_count
                    last_count = count
                else:
                    if current.val < previous.val and current.val < next.val:
                        array.append(count)
                        if last_count>0:
                            if min_dist == 0:
                                min_dist = count-last_count
                            elif count-last_count<min_dist:
                                min_dist = count-last_count
                        last_count = count
            
            previous = current
            current = next
            count = count+1
        dist_array.append(min_dist)
        if len(array)<2:
            return [-1,-1]
        else:
            dist_array.append(array[len(array)-1]-array[0])
            return dist_array