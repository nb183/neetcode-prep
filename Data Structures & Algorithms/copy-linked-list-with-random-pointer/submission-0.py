"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        current = head
        while current:
            copy_head = Node(current.val)
            mp[current] = copy_head
            current = current.next

        current = head
        while current:
            mp[current].next = mp[current.next]
            mp[current].random = mp[current.random]
            current = current.next
        
        return mp[head]


        
            






