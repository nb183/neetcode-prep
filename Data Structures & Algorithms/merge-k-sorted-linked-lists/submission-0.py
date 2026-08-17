# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # heapq.heappush(heap, elem)
        # heapq.heappop(heap)
        # heapq.heapify(heap)

        dummy = ListNode()
        prev = dummy

        for i in range(len(lists)):
            while(lists[i]):
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next

        while heap:
            small = heapq.heappop(heap)
            new_node = ListNode(small)
            prev.next = new_node
            prev = new_node
        
        return dummy.next