# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next


# # will give tle
# class Solution1 :
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         ans = ListNode()
#         temp = ans
#         kptrs = []
        
#         for i in range(len(lists)):
#             kptrs.append(lists[i])
#         # print(kptrs)
        
#         def findSmallest(kptrs):
#             smallest = None
            
#             for i in range(len(kptrs)):
#                 if kptrs[i]:
#                     smallest = i
#                     break
                    
#             for i in range(len(kptrs)):
#                 if(kptrs[i] and kptrs[i].val < kptrs[smallest].val):
#                     smallest = i
                    
#             return smallest
            

#         minHeap = []
#         for i in range(len(lists)):
            
#         smallest = findSmallest(kptrs)
#         while(smallest!=None):
#             temp.next = ListNode(kptrs[smallest].val)
#             kptrs[smallest] = kptrs[smallest].next
#             temp = temp.next
#             smallest = findSmallest(kptrs)
#         return ans.next
    
    
#using minHeap
class Solution :
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        minHeap = []
        for i in range(len(lists)):
            if(lists[i]):
                heappush(minHeap, (lists[i].val, i))
        while(minHeap):
            val, index = heappop(minHeap)
            temp.next = ListNode(val)
            temp = temp.next
            node = lists[index]
            node = node.next
            lists[index] = node
            if node:
                heappush(minHeap, (node.val, index))
        return ans.next
    
            
        