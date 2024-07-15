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
        if not head:
            return None
        
        hashmap = {}

        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            hashmap[curr].next = hashmap.get(curr.next)
            hashmap[curr].random = hashmap.get(curr.random)
            curr = curr.next

        return hashmap[head]

        #oldnode1 <-> newnode 1  hashmap[curr] = newnode 1.next = hashmap(oldnode1.next) = newnode2
        #oldnode2 <-> newnode 2
        #oldnode3 <-> newnode 3
        # same thing with pointer

        
