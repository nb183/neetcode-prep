# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1, 2, 3, 4, 5, 6, 7] n = 5

        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = dummy


        while n > 0:
            right = right.next
            n -= 1

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

        
        