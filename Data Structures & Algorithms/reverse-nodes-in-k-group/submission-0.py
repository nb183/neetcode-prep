# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
                
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        groups = count // k
        total_reverse = groups * k

        prev_last = dummy
        curr = head
        curr_count = 0
        prev = None

        while curr:
            curr_count += 1

            if (curr_count - 1) % k == 0:
                prev = None
                first = curr

            next_node = curr.next
            curr.next = prev
            prev = curr

            if curr_count % k == 0:
                prev_last.next = curr
                first.next = next_node
                prev_last = first

            if curr_count == total_reverse:
                break
            curr = next_node

        if curr_count == total_reverse:
            prev_last = curr

        return dummy.next


        