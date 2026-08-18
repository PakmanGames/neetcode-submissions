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
        mappings = {}
        curr = head
        while curr:
            new = Node(curr.val)
            mappings[curr] = new
            curr = curr.next

        curr = head
        while curr:
            new = mappings[curr]
            new.next = mappings.get(curr.next, None)
            new.random = mappings.get(curr.random, None)
            curr = curr.next
        
        return mappings.get(head, None)
    