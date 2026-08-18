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
        cloned = {}

        self.dfs(node, cloned)
        return cloned[node]
    
    def dfs(self, node, cloned):
        if not node:
            return None
        if node in cloned:
            return cloned[node]
        new = Node(node.val)
        cloned[node] = new
        for neigh in node.neighbors:
            new.neighbors.append(self.dfs(neigh, cloned))
        return new
    # Space: O(V)
    # Time: O(E + V), traverse every edge and vertex at least once