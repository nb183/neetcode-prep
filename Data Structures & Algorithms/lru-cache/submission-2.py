class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.prev, self.tail.next = self.tail, self.head

    
    def insert_at_front(self, node):
        node.next = self.head
        node.prev = self.head.prev

        self.head.prev.next = node
        self.head.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        node = self.mp[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        self.insert_at_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            node = self.mp[key]
            node.value = value

            node.prev.next = node.next
            node.next.prev = node.prev

            self.insert_at_front(node)

            return

        if len(self.mp) == self.capacity:
            least = self.tail.next

            self.tail.next = least.next
            least.next.prev = self.tail

            del self.mp[least.key]

        node = Node(key, value)
        
        self.insert_at_front(node)

        self.mp[key] = node
    
            


            














        
