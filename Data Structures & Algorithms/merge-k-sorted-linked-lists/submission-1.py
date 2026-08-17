# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy

        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))

        while pq:
            minm, index = heapq.heappop(pq)
            prev.next = lists[index]
            prev = prev.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(pq, (lists[index].val, index))
        return dummy.next
            