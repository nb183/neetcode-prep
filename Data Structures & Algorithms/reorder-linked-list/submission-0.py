# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow.next
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        start = head

        while prev:
            start_next, end_next = start.next, prev.next
            start.next = prev
            prev.next = start_next
            prev, start = end_next, start_next

        start.next = None
