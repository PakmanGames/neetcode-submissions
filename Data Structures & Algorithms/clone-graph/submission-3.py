"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {} # O(V) space
        def clone(n, stored):
            if n in stored: # O(V)
                return stored[n]
            new = Node(n.val)
            for neigh in n.neighbors: # O(E)
                stored[n] = new
                new.neighbors.append(clone(neigh, stored))
            return new
        return clone(node, cloned)
        # Time O(V + E), Space O(V)